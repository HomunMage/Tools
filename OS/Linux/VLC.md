# VLC

## Costmized vlc toolbar

To back up your customized VLC toolbar, you'll need to save the VLC configuration file where your settings are stored. Here’s how you can do it:

### Steps to Backup Customized VLC Toolbar

1. **Locate VLC's Configuration Folder**:
   - The location of the configuration folder varies depending on your operating system.

   - **Windows**:
     - Navigate to `C:\Users\<YourUsername>\AppData\Roaming\vlc`
   - **macOS**:
     - Go to `~/Library/Preferences/org.videolan.vlc`
   - **Server**:
     - Look in `~/.config/vlc`

2. **Backup the Configuration Files**:
   - Inside the configuration folder, find the `vlcrc` file (this contains settings for VLC, including toolbar customizations).
   - You may also want to back up the entire folder to ensure you capture all custom settings.

3. **Copy the Files**:
   - Copy the `vlcrc` file and any other files from the VLC configuration folder to a backup location (such as an external drive or cloud storage).

4. **Restore the Toolbar**:
   - To restore your customized toolbar later, simply replace the existing `vlcrc` file in the VLC configuration folder with your backed-up version. You might need to restart VLC for the changes to take effect.

### Additional Notes

- **Exporting and Importing Toolbar Settings**: If you want to export your customized toolbar specifically:
  1. Go to **View > Customize Interface** in VLC.
  2. Look for any options that allow you to export the toolbar settings directly (though this may not be available in all versions).

- **VLC Versions**: Keep in mind that different versions of VLC may have slight variations in where these settings are stored, so it's a good idea to check the documentation for your specific version if you run into issues.

By following these steps, you should be able to successfully back up your customized VLC toolbar and restore it whenever needed.

## Set to english

run with env
```
LANGUAGE=en vlc
```

### defualt eng

#### Create a Custom Script
1. Open a Terminal.
2. Create a New VLC Desktop Entry:
    * First, create a new script that launches VLC in English:
        ```
        nano ~/open-vlc-en.sh
        ```
    * Add the following lines to the script:
        ```
        #!/bin/bash
        env LANG=en_US.UTF-8 vlc "$@"
        ```
3. Make the Script Executable:
    ```
    chmod +x ~/open-vlc-en.sh
    ```
4. Create a New Desktop Entry for the Script:
    * Now create a ```.desktop``` file to register this script as an application:
        ```
        nano ~/.local/share/applications/open-vlc-en.desktop
        ```
    * Add the following content:
        ```
        [Desktop Entry]
        Version=1.0
        Name=Open VLC in English
        Exec=/home/yourusername/open-vlc-en.sh %U
        Type=Application
        Terminal=false
        MimeType=video/mp4;video/x-matroska;video/x-msvideo;video/avi;video/x-flv;video/x-ms-wmv;video/x-mpeg;video/x-mpeg2;
        ```
    * Replace ```yourusername``` with your actual username.
5. Update the Desktop Database:
    ```
    update-desktop-database ~/.local/share/applications/
    ```
6. Set Default Application for Video Files:
* Now, right-click on any video file (e.g., ```.mp4```, ```.avi```, etc.) and select Properties.
* Go to the **Open With** tab.
* You should see **Open VLC in English** listed. Select it and click on **Set as Default**.
* If it’s not listed, click on Add and navigate to the ```open-vlc-en.desktop``` file you created.



## Streaming on Network
**Use VLC Media Player for Streaming**
VLC is a powerful tool available on both Linux and Windows. It can be used to stream media files from one device to another over the network.

**Share Server (PC):**
   - Open VLC.
   - Click on **Media** > **Stream...**.
   - Click **Add** and choose the **MP4 file** you want to stream.
   - Click **Stream** at the bottom right.
   - In the next window, click **Next**.
   - In the "Destination Setup", choose **HTTP** from the drop-down menu.
   - Click **Add** and set the port (e.g., 8080).
   - You can leave the path as `/` or change it if you prefer.
   - Select **Next** and choose the proper transcoding options, like H.264 for video and MP3 for audio (or leave it as default).
   - Click **Stream**.

**For Client:**
   - Open VLC on your Windows notebook.
   - Click **Media** > **Open Network Stream**.
   - Enter the network URL of your Server PC in the form of `http://<Server-IP>:<port>`, for example: `http://192.168.1.100:8080`.
   - Click **Play**, and the streamed video from your Server PC should start playing.