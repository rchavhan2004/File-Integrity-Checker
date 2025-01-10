<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Integrity Checker</title>
</head>
<body>

<h1>File Integrity Checker</h1>

<p>This Python project calculates the SHA-256 hash for files in a given directory to verify their integrity. It traverses the directory and subdirectories, reads each file, and calculates its hash, which can be used to check if the files have been altered.</p>

<h2>Features</h2>
<ul>
    <li>Traverse any given directory and its subdirectories.</li>
    <li>Calculate SHA-256 hash for each file.</li>
    <li>Display the file path and corresponding SHA-256 hash.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>hashlib</code> and <code>os</code> libraries (both are part of the standard Python library)</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/your-username/file-integrity-checker.git
cd file-integrity-checker</code></pre>
    </li>
    <li>Ensure you have Python 3.x installed on your system. If not, download and install it from the official <a href="https://www.python.org/downloads/">Python website</a>.</li>
</ol>

<h2>Usage</h2>
<ol>
    <li>After cloning the repository, navigate to the project folder.</li>
    <li>Run the <code>File_integrity_checker.py</code> script:
        <pre><code>python File_integrity_checker.py</code></pre>
    </li>
    <li>Enter the directory path for which you want to check the file integrity. The script will output the SHA-256 hash of each file in the directory and its subdirectories.
        <pre><code>Enter the directory path: C:\example\directory</code></pre>
    </li>
</ol>

<h2>Example Output</h2>
<pre><code>Enter the directory path: C:\example\directory
File: C:\example\directory\file1.txt
SHA-256 HASH: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
File: C:\example\directory\subdir\file2.jpg
SHA-256 HASH: c5c5e6a69e9e8f034cb5a67dcf0c0c2d484d3ec63df19c38e4a6ed3f4384c11b</code></pre>

<h2>How it works</h2>
<ol>
    <li><strong><code>calculate_sha256(filepath)</code></strong>: This function calculates the SHA-256 hash for the file specified by the <code>filepath</code>.</li>
    <li><strong><code>check_integrity(directory_path)</code></strong>: This function checks if the specified directory exists and is a valid directory. It then traverses the directory and calculates the SHA-256 hash for each file.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributions</h2>
<p>Feel free to fork this project and submit pull requests with improvements or bug fixes. If you encounter any issues or have suggestions for enhancements, please open an issue in the GitHub repository.</p>

</body>
</html>
