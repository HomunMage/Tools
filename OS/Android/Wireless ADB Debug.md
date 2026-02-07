# Wireless ADB Over SSH Tunnel, Wifi Debug Android

If your Android phone is on a mobile (4G/5G) network and your Linux PC is on a wired PPPoE connection, they can't see each other on the same LAN — which means Android's Wireless Debugging won't work out of the box. This guide shows how to bridge that gap using an SSH reverse tunnel.

## The Problem

Android 11+ introduced **Wireless Debugging**, which lets you use ADB over Wi-Fi without a USB cable. However, it relies on both devices being on the same local network. If your phone is on cellular data and your PC is on a separate broadband connection, the phone's local IP (e.g., `192.168.50.17`) is unreachable from your PC.

## The Solution: SSH Reverse Tunnel

The idea is simple: use an SSH connection from your phone to your PC, and set up **reverse port forwarding** (`-R`) to tunnel the wireless debugging ports back to your PC's `localhost`.

### Why Reverse (`-R`) and Not Local (`-L`)?

Since the phone initiates the SSH connection to the PC, we need the tunnel to expose the phone's ports on the PC side:

- **`-R` (reverse forwarding):** "Make a port on the SSH server (PC) forward to a port on the SSH client (phone)." This is what we need — the phone's debugging service becomes accessible on the PC's localhost.
- **`-L` (local forwarding):** "Make a port on the SSH client forward to a port on the SSH server." This would go the wrong direction for our use case.

## Prerequisites

- An Android phone with **Developer Options** and **Wireless Debugging** enabled
- A Linux PC with a public IP (or at least reachable from the phone's network)
- An SSH client on the phone (e.g., ConnectBot, Termux, or JuiceSSH)
- ADB installed on the PC (`sudo apt install android-tools-adb` or download Google's platform-tools)

## Understanding the Ports

Wireless Debugging uses **two separate ports**, but never at the same time:

| Port | Purpose | Lifetime |
|------|---------|----------|
| **Connect port** (e.g., 37673) | Used by `adb connect` for the actual debugging session | Persistent while Wireless Debugging is on (may change on restart) |
| **Pairing port** (random) | Used by `adb pair` for one-time device pairing | Temporary — only exists while the pairing dialog is open |

You only need to pair once. After that, you just need the connect port.

## Step-by-Step Setup

### Step 1: Enable Wireless Debugging on the Phone

1. Go to **Settings → Developer Options**
2. Turn on **Wireless Debugging**
3. Note the **IP address and port** shown (e.g., `192.168.50.17:37673`) — this is your connect port

### Step 2: First-Time Pairing

If you haven't paired your PC with the phone yet, you'll need to tunnel **both** ports.

On the phone, tap **"Pair device with pairing code"**. The phone will display a six-digit pairing code and a temporary pairing port (e.g., `38857`).

Now set up the SSH tunnel from the phone with both ports:

```bash
ssh -R 37673:localhost:37673 -R 38857:localhost:38857 user@your-pc-ip
```

On the PC, pair using the **pairing port** (not the connect port):

```bash
adb pair localhost:38857
# Enter the six-digit pairing code when prompted
```

You should see:

```
Successfully paired to localhost:38857 [guid=adb-XXXXXXXXXXXX-XXXXXX]
```

> **Common mistake:** Don't try to `adb pair` with the connect port (37673). That will fail with `error: protocol fault (couldn't read status message): Success`. The connect port is only for `adb connect`.

### Step 3: Connect

After pairing succeeds, connect using the **connect port**:

```bash
adb connect localhost:37673
# Expected output: connected to localhost:37673
```

Verify the connection:

```bash
adb devices
# Expected output:
# List of devices attached
# localhost:37673    device
```

### Step 4: Subsequent Connections (After First Pairing)

Once paired, you don't need to pair again. For future sessions, you only need to tunnel the connect port:

```bash
# On the phone:
ssh -R 37673:localhost:37673 user@your-pc-ip

# On the PC:
adb connect localhost:37673
```

## Troubleshooting

### `error: protocol fault (couldn't read status message): Success`

This usually means one of:

- **You're connecting to the wrong port** — make sure you use the pairing port for `adb pair` and the connect port for `adb connect`
- **ADB version mismatch** — update ADB on your PC to match your phone's Android version. Check with `adb --version`
- **The tunnel isn't established** — verify the SSH connection is active and the port forwarding is correct

### `adb devices` shows `unauthorized`

Check your phone for an authorization dialog and approve it. If you don't see one, try revoking USB debugging authorizations in Developer Options and reconnecting.

### Connect port changed

The connect port (e.g., 37673) may change each time you toggle Wireless Debugging off and on. Always check the current port in **Settings → Developer Options → Wireless Debugging** before setting up the tunnel.

## Quick Reference

```bash
# First time (pairing + connecting):
# Phone → PC SSH:
ssh -R 37673:localhost:37673 -R <pairing-port>:localhost:<pairing-port> user@pc-ip

# PC:
adb pair localhost:<pairing-port>      # enter 6-digit code
adb connect localhost:37673

# After first pairing:
# Phone → PC SSH:
ssh -R 37673:localhost:37673 user@pc-ip

# PC:
adb connect localhost:37673
adb devices
```

## Summary

The key insight is understanding the direction of the SSH tunnel. Since the phone connects to the PC via SSH, you need **reverse forwarding** (`-R`) to make the phone's wireless debugging ports accessible on the PC's localhost. Pairing only needs to happen once, and after that you only need to forward a single port for day-to-day use.