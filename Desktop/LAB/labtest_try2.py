import ssl
import socket

def get_remote_certificate(hostname, port=443):
    """Retrieve the SSL certificate from the server."""
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.connect((hostname, port))
    cert = conn.getpeercert(binary_form=True)  # Retrieve the certificate in binary form
    conn.close()
    return cert

def load_local_certificate(cert_file):
    """Load and convert the local PEM certificate to binary (DER) format."""
    with open(cert_file, 'rb') as f:
        pem_cert = f.read()

    # Convert PEM to DER format
    return ssl.PEM_cert_to_DER_cert(pem_cert.decode('utf-8'))

def validate_certificate(hostname, cert_file):
    """Compare the local and remote SSL certificates."""
    remote_cert = get_remote_certificate(hostname)
    local_cert = load_local_certificate(cert_file)

    # Compare the raw bytes of both certificates
    if remote_cert == local_cert:
        print("SSL certificates match.")
        return True
    else:
        print("SSL certificates do not match!")
        return False

if __name__ == "__main__":
    hostname = '60a21d3f745cd70017576092.mockapi.io'
    cert_file_path = 'mockapi_cert.pem'
    
    result = validate_certificate(hostname, cert_file_path)
    if result:
        print("Test Passed: SSL certificate is valid")
    else:
        print("Test Failed: SSL certificate does not match!")
