# UTF-8 Validation

UTF-8 validation is a process to determine whether a given sequence of bytes is a valid UTF-8 encoded string or not. UTF-8 is a variable-length character encoding standard that can represent almost all characters in the Unicode standard.

## Key Rules for UTF-8 Validation

1. **ASCII Characters (U+0000 to U+007F):** In UTF-8, ASCII characters are represented as single bytes with values from 0 to 127 (U+0000 to U+007F). These are the only characters that can be represented using a single byte in UTF-8.

2. **Multibyte Characters (U+0080 to U+10FFFF):** Characters outside the ASCII range (U+0080 to U+10FFFF) are represented using multiple bytes. The number of bytes used depends on the character's code point:
   - 2 bytes: U+0080 to U+07FF
   - 3 bytes: U+0800 to U+FFFF
   - 4 bytes: U+10000 to U+10FFFF

3. **Byte Sequences for Multibyte Characters:** The bytes of a multibyte character have specific patterns to indicate the start and continuation of the character. For a multibyte character, the first byte always starts with a pattern of '11' followed by '0's, and continuation bytes start with '10'. The remaining bits are used to represent the character's code point.

4. **Overlong Encodings:** Overlong encodings are invalid representations of characters, where the character is represented using more bytes than necessary. For example, representing the ASCII character 'A' (U+0041) as two bytes rather than one. UTF-8 validation should detect and reject overlong encodings.

5. **Invalid Sequences:** Some byte sequences are reserved and should not appear in valid UTF-8 encoded strings. For example, the byte sequence 'FE' and 'FF' should not appear as they are not used in UTF-8.

6. **Code Point Limits:** UTF-8 encoding must not go beyond the valid Unicode code point range (U+0000 to U+10FFFF).

## Usage

When validating a sequence of bytes as UTF-8, you would need to check if it adheres to these rules. If the byte sequence follows all the rules, then it is a valid UTF-8 encoded string. Otherwise, it is considered invalid and should not be used as a UTF-8 encoded string.

### Example (Python)

Here's a simple Python function to check if a given byte sequence is valid UTF-8:

```python
def is_valid_utf8(byte_sequence):
    try:
        byte_sequence.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
```
