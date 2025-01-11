# 🔐 File Integrity Checker</h1>

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2917/2917995.png" alt="File Integrity Icon" width="120">
</p>

<p align="center">
  <strong>🔍 An Educational Tool to Verify File Integrity and Prevent Unauthorized Changes</strong>
</p>

---

## ⚡ Overview

Welcome to the *File Integrity Checker Project*!  
This project serves as a cybersecurity tool for monitoring file integrity and ensuring files have not been tampered with. Through this project, I aim to explore:

- ✅ How to calculate SHA-256 hashes for files.
- ✅ Techniques for verifying file integrity through hash comparison.
- ✅ Methods to detect unauthorized changes in files.
- ✅ Real-time hashing for multiple files in directories.

> *⚠ Important:* This project is intended for *educational purposes* to understand the significance of file integrity and security measures.

---

## 🛠 Features

- 🖥 *SHA-256 hashing* for verifying file integrity
- 🔒 *Directory scanning* to check the integrity of files
- 📄 *File path and hash display* for easy reference
- 🚀 *Cross-platform support* (Windows/Linux/Mac)
- ⚙️ *Customizable* for different file types and directories

---

## 📂 Project Structure

| File/Folder               | Description                                 |
|----------------------------|---------------------------------------------|
| `File_integrity_checker.py` | Main Python script for file integrity check |
| `requirements.txt`         | List of Python dependencies                 |
| `README.html`              | Project documentation                      |

---

<h2>🔑 How It Works</h2>

1. **`calculate_sha256(filepath)`**: This function calculates the SHA-256 hash for the file located at the provided `filepath`.
2. **`check_integrity(directory_path)`**: This function scans the specified directory for files and calculates the SHA-256 hash for each one to check integrity.

---

<h2>🛠 Usage</h2>
<ol>
    <li>Run the file integrity checker script:
        <pre><code>python File_integrity_checker.py</code></pre>
    </li>
    <li>Enter the path of the directory to scan for file integrity.</li>
    <li>The script will output the SHA-256 hash of each file, which can be used to check if any file has been modified.
        <pre><code>Enter the directory path: C:\example\directory</code></pre>
    </li>
</ol>

<h2>💬 Example Output</h2>
<pre><code>Enter the directory path: C:\example\directory
File: C:\example\directory\file1.txt
SHA-256 HASH: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
File: C:\example\directory\subdir\file2.jpg
SHA-256 HASH: c5c5e6a69e9e8f034cb5a67dcf0c0c2d484d3ec63df19c38e4a6ed3f4384c11b</code></pre>

<p align="center">
  <strong>🔐 Secure your files with integrity checks—protect your data. 🔒</strong>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4d3ca049-9d98-4490-933e-576e683792c7" alt="Secure Icon" width="80">
</p>

</body>
</html>
