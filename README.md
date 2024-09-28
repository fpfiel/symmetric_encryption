# Trivial symmetric blockalgorithm for encryption/decryption


`A.1. Implementierung eines symmetrischen Verschlüsselungsverfahrens
Es ist mit einer Programmier-/Skriptsprache nach Wahl (vorzugsweise Perl) ein primitiver symmetrischer Blockalgorithmus zu entwickeln, der die grundlegenden Elemente symmetrischer Verfahren anwendet (Aufteilung in Blöcke, Transposition, Substitution, Schlüsselintegration). Im Zuge der Präsentation ist die Funktionsweise durch die Verschlüsselung- bzw. Entschlüsselung eines Textes live vorzuführen.`


Disclaimer: This is a non-optimized algorithm meant only to demonstrate the basic workflow of a symmetric block algorithm. I am aware that various aspects can be improved, such as the use of base64, strings instead of bytearrays, etc.

## Files

### encryption.py
Contains the actual algorithm for encryption and decryption. All components of the algorithm itself are placed here.
It provides two methods:
- encryption(clear_text: str, key: str, rounds: int)
- decryption(cipher_text: str, key: str, rounds: int)

In order to encrypt-decrypt a value, the same key and the same count of rounds must be used.

### main.py
Allows you to specify the value, key, and number of rounds. It demonstrates how the functions should be executed. This is the entry point for debugging if one wants to trace the execution flow.

### encryption_test.py
Contains tests for the different components of the algorithm and the encrypt-decrypt flow.

### symm_encryption.py
Was intended to be a simple CLI to encrypt and decrypt values from the command line. Since I didn’t use base64, this didn’t work. I might fix it later.
