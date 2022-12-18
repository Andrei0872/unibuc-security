1. Parolele nu trebuie stocate in *plaintext*.
2. Nu se expun erorile care pot divulga aspecte referitoare la sistem.
3. Preventie impotriva *SQL-injection*.

---

1. [1](https://github.com/inginerie-software-22-23/proiect-inginerie-software-pdf-destroyers/blob/abaa8800538485eb85c9b3a6f4d09d81a66f0dc3/server/auth/auth.service.js#L14).
2. [1](https://github.com/inginerie-software-22-23/proiect-inginerie-software-pdf-destroyers/blob/abaa8800538485eb85c9b3a6f4d09d81a66f0dc3/server/auth/auth.service.js#L11), [2](https://github.com/inginerie-software-22-23/proiect-inginerie-software-pdf-destroyers/blob/abaa8800538485eb85c9b3a6f4d09d81a66f0dc3/server/auth/auth.service.js#L16).
3. `userRepository.findByEmail` -> [`pool.query()`](https://github.com/inginerie-software-22-23/proiect-inginerie-software-pdf-destroyers/blob/abaa8800538485eb85c9b3a6f4d09d81a66f0dc3/server/user/user.repository.js#L18-L19). [Parameterized queries](https://node-postgres.com/features/queries#parameterized-query).