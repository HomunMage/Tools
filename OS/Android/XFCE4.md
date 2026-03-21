# Run XFCE4 Desktop on Android via Termux

## Prerequisites

- Android 8+ device, RAM >= 8GB, storage > 10GB
- Install **Termux** (from F-Droid)
- Install **Termux X11** (from [GitHub Releases](https://github.com/nicedayzhu/termux-x11/releases))

## 1. Install Packages in Termux

```bash
pkg update -y && pkg upgrade -y
pkg install -y x11-repo
pkg install -y termux-x11-nightly proot-distro pulseaudio virglrenderer-android
```

## 2. Install Ubuntu via Proot

```bash
proot-distro install ubuntu
```

## 3. Install XFCE4 & VS Code in Ubuntu

```bash
proot-distro login ubuntu --shared-tmp -- bash -c '
export DEBIAN_FRONTEND=noninteractive
apt update -y && apt upgrade -y
apt install -y xfce4 xfce4-terminal dbus-x11 sudo --no-install-recommends
apt install -y wget
wget -O /tmp/code.deb "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64"
apt install -y /tmp/code.deb
rm -f /tmp/code.deb
'
```

> **Note:** If `elementary-xfce-icon-theme` gets stuck during install, kill it with `pkill -f "icon-theme"` in another Termux session, then run `dpkg --remove --force-remove-reinstreq elementary-xfce-icon-theme` inside proot to skip it.

## 4. Start Script

Save as `~/.shortcuts/startproot_debian.sh`:

```bash
#!/bin/bash

killall -9 termux-x11 pulseaudio virgl_test_server_android termux-wake-lock

am start --user 0 -n com.termux.x11/com.termux.x11.MainActivity
XDG_RUNTIME_DIR=${TMPDIR}
termux-x11 :0 -ac &
sleep 3

pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1
pacmd load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1

virgl_test_server_android &

proot-distro login ubuntu --shared-tmp -- bash -c "export DISPLAY=:0 PULSE_SERVER=tcp:127.0.0.1; GALLIUM_DRIVER=virpipe dbus-launch --exit-with-session startxfce4"
```

```bash
chmod +x ~/.shortcuts/startproot_debian.sh
```

## 5. Usage

1. Open **Termux**
2. Run `bash ~/.shortcuts/startproot_debian.sh`
3. Switch to **Termux X11** app — XFCE4 desktop appears

### Launch VS Code

In XFCE4 terminal:
```bash
code --no-sandbox
```

### Desktop Shortcuts

Create VS Code shortcut:
```bash
cat > ~/Desktop/vscode.desktop << 'EOF'
[Desktop Entry]
Name=VS Code
Exec=/usr/bin/code --no-sandbox
Icon=code
Type=Application
Terminal=false
EOF
chmod +x ~/Desktop/vscode.desktop
```

Create terminal shortcut:
```bash
cat > ~/Desktop/terminal.desktop << 'EOF'
[Desktop Entry]
Name=Terminal
Exec=xfce4-terminal
Icon=utilities-terminal
Type=Application
Terminal=false
EOF
chmod +x ~/Desktop/terminal.desktop
```

## 6. Settings

- **Resolution:** Termux X11 → Preferences → Display resolution mode → set custom resolution (e.g. 1280x720)
- **Touch mode:** Termux X11 → Preferences → switch to "Simulated touchpad"
- **GPU acceleration:** Already enabled via `virgl_test_server_android` and `GALLIUM_DRIVER=virpipe` in the start script
- **CJK input:** Termux X11 → Preferences → Keyboard → enable "Workaround to enable CJK Gboard"

## Wireless ADB (Optional)

For remote management from PC:

```bash
adb pair localhost:<pair_port>    # enter pairing code
adb connect localhost:<connect_port>
```

> Wireless ADB can be unstable. USB connection is more reliable.
