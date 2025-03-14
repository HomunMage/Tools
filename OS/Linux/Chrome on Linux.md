# Install Chrome on Linux Mint

source: https://www.digitalocean.com/community/tutorials/install-chrome-on-linux-mint


**Chrome (Official):**

1.  **Key:**
    ```bash
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    ```
2.  **Repo:**
    ```bash
    sudo add-apt-repository "deb http://dl.google.com/linux/chrome/deb/ stable main"
    ```
3.  **Update:**
    ```bash
    sudo apt update
    ```
4.  **Install:**
    ```bash
    sudo apt install google-chrome-stable
    ```
5. **Run:** type in the terminal `google-chrome` or just find it in your applications menu

**Chromium (Open Source):**

```bash
sudo apt install chromium-browser
```
**Run:** Just find it in your applications menu

**Uninstall (Chrome):**

```bash
sudo apt remove google-chrome-stable
```

**Notes:**

*   Open terminal for commands.
*   Type `y` when prompted for confirmation.
