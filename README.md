Caesar Cypher

Playing around with cyphers. This is the caesar cypher that just shifts the plain text a number of characters along the alphabet.
<P>
So the 'normal' alphabet abcdefghijklmnopq... would look like fghijklmnopqrst if shifted 5 characters.
<>
The program excepts all printable characters.
<p>
encoding "the quick brown fox jumps over the lazy dog 01234567890"
with a shift of 5 results in "ymjvznhpgwtBsktCozruxtAjwymjqfEDitl56789abcde5"

### screen grab
```text
  ____                              ____            _
 / ___|__ _  ___  ___  __ _ _ __   / ___|   _ _ __ | |__   ___ _ __
| |   / _` |/ _ \/ __|/ _` | '__| | |  | | | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |    | |__| |_| | |_) | | | |  __/ |
 \____\__,_|\___||___/\__,_|_|     \____\__, | .__/|_| |_|\___|_|
                                        |___/|_|
Type 'encode' to encrypt, type 'decode' to decrypt:
e
Type your message:
The Quick Brown Fox Jumps Over The Lazy Dog 0123456789
Type the shift number:
5
YmjVznhpGwtBsKtCOzruxTAjwYmjQfEDItl56789abcde

```
```text
  ____                              ____            _
 / ___|__ _  ___  ___  __ _ _ __   / ___|   _ _ __ | |__   ___ _ __
| |   / _` |/ _ \/ __|/ _` | '__| | |  | | | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |    | |__| |_| | |_) | | | |  __/ |
 \____\__,_|\___||___/\__,_|_|     \____\__, | .__/|_| |_|\___|_|
                                        |___/|_|
Type 'encode' to encrypt, type 'decode' to decrypt:
d
Type your message:
YmjVznhpGwtBsKtCOzruxTAjwYmjQfEDItl56789abcde
Type the shift number:
5
The Quick Brown Fox Jumps Over The Lazy Dog 0123456789
```
