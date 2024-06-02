# QR Code Generator

<script src="{{ '/assets/js/GenQRCode.js' | relative_url }}" defer></script>

<label for="urlInput">Enter URL:</label>
<input type="text" id="urlInput" placeholder="Enter URL here">
<button id="generateBtn">Generate QR Code</button>
<div id="qrcode"></div>
<button id="downloadWebpBtn" style="display:none;">Download as WEBP</button>
<button id="downloadPngBtn" style="display:none;">Download as PNG</button>