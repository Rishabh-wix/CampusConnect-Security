# CampusConnect Security Assignment

## Student Details

**Name:** Rishabh Srivastava

---

# Part 1

## RSA Implementation

This project implements the RSA algorithm.

### Features
- Accepts two prime numbers p and q.
- Calculates:
  - n = p × q
  - φ(n) = (p − 1)(q − 1)
- Selects a valid public exponent e.
- Computes private exponent d.
- Encrypts a plaintext message.
- Decrypts the ciphertext back to the original message.
- Includes:
  - Assignment example
  - One additional custom example

---

## Diffie-Hellman Key Exchange

This project also implements the Diffie-Hellman Key Exchange algorithm.

### Features

- Accepts public prime p.
- Accepts public base α.
- Accepts Alice's and Bob's private keys.
- Generates public keys.
- Computes the shared secret independently.
- Demonstrates that both parties generate the same shared secret.
- Includes:
  - Assignment example
  - One additional custom example

---

# Part 2

## Security Principle Mapping

### RSA

RSA provides **confidentiality** by encrypting sensitive data using a public key. Only the private key owner can decrypt the message. It can also provide **authentication** and **non-repudiation** when used with digital signatures.

### Diffie-Hellman

Diffie-Hellman provides **secure key exchange**. It allows two users to establish a common secret key over an insecure network without transmitting the secret key directly. It is not an encryption algorithm.

---

# Threat Model Write-up

## (a) Firewall Recommendation

A firewall should be placed between the Internet and the CampusConnect application server.

A **hardware firewall** is recommended because it protects the entire network.

Traffic Rule:
- Allow only HTTPS (Port 443)
- Block all unnecessary incoming ports.

---

## (b) Intrusion Detection System

CampusConnect should use **both Host-based IDS (HIDS) and Network-based IDS (NIDS).**

- HIDS detects suspicious activities on the server.
- NIDS monitors malicious network traffic.

Using both provides better protection.

---

## (c) HTTP vs HTTPS

CampusConnect should use **HTTPS** instead of HTTP.

HTTPS encrypts communication using TLS and prevents:

- Credential Sniffing
- Session Hijacking
- Man-in-the-Middle (MITM) attacks

---

## (d) Authentication Design

CampusConnect should implement **Multi-Factor Authentication (MFA).**

Two authentication factors:

1. Password
2. OTP generated through Authenticator App or Email

Permissions:

- Student
  - View Courses
  - Register Courses
  - View Grades

- Instructor
  - Manage Courses
  - Upload Grades
  - View Students

- Admin
  - Full System Access
  - Manage Users
  - Manage Database

This follows the **Least Privilege Principle**, where each user gets only the permissions required.

---

## (e) Attack Classification

Example Attack:

**Man-in-the-Middle (MITM) Attack**

Classification:

**Active Attack**

Reason:

The attacker intercepts and modifies communication between the client and server.

HTTPS prevents this attack by encrypting network traffic.

---

# Conclusion

RSA ensures secure encryption, while Diffie-Hellman securely exchanges secret keys. HTTPS, Firewall, IDS, Least Privilege, and Multi-Factor Authentication together improve the overall security of the CampusConnect system.
