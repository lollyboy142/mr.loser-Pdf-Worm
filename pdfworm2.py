import shutil
import os
from reportlab.pdfgen import canvas
import subprocess

# Path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Path to the output PDF file
output_pdf_path = os.path.join(downloads_folder, "mr_loser_was_here_2025.pdf")

# Create the PDF
c = canvas.Canvas(output_pdf_path)
c.drawString(100, 750, "mr.loser was here 2025")  # Position the text on the page
c.save()

print(f"PDF created at {output_pdf_path}")

# Create a shared folder on the local computer
shared_folder_path = os.path.expanduser("~/sharedfiles")
os.makedirs(shared_folder_path, exist_ok=True)  # Create the folder if it doesn't exist

# Copy the PDF file to the shared folder
shutil.copy(output_pdf_path, shared_folder_path)
print(f"Copied {output_pdf_path} to {shared_folder_path}")

# Set permissions for the shared folder
os.chmod(shared_folder_path, 0o777)  # Make the folder accessible to everyone
print(f"Set permissions for {shared_folder_path} to shared (777)")

# Configure Samba to share the folder
samba_config = f"""
[sharedfiles]
   path = {shared_folder_path}
   browseable = yes
   writable = yes
   guest ok = yes
   create mask = 0777
   directory mask = 0777
"""

# Append the Samba configuration to smb.conf
smb_conf_path = "/etc/samba/smb.conf"
try:
    with open(smb_conf_path, "a") as smb_conf:
        smb_conf.write(samba_config)
    print("Samba configuration updated.")
except PermissionError:
    print(f"Permission denied: Unable to write to {smb_conf_path}. Run the script with sudo.")

# Restart Samba service to apply changes
try:
    subprocess.run(["sudo", "systemctl", "restart", "smbd"], check=True)
    print("Samba service restarted.")
except Exception as e:
    print(f"Failed to restart Samba service: {e}")