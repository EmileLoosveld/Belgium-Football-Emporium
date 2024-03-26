CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  price INTEGER  NOT NULL,
  image BLOB NOT NULL
);

INSERT INTO items (name, description, price, image) VALUES
    ('Voetbalshirt', 'Officieel voetbalshirt van de nationale ploeg van België', 50, '1.png'),
    ('Mok', 'Mok met het logo van de nationale ploeg van België', 8, '2.png'),
    ('Sleutelhanger', 'Sleutelhanger met het embleem van de nationale ploeg van België', 5, '3.png'),
    ('Voetbal', 'Voetbal in de kleuren van de nationale ploeg van België', 20, '4.png'),
    ('Sjaal', 'Sjaal in de kleuren van de nationale ploeg van België', 15, '5.png'),
    ('Pet', 'Pet met het logo van de nationale ploeg van België', 10, '6.png'),
    ('Flag', 'dsctf{S3cur1ty_sa1d_1t_wa$_0k!} ', 20, '7.png'),
    ('T-shirt', 'T-shirt met het logo van de nationale ploeg van België', 25, '8.png'),
    ('Sokken', 'Sokken in de kleuren van de nationale ploeg van België', 10, '9.png'),
    ('Rugzak', 'Rugzak met het logo van de nationale ploeg van België', 30, '10.png');

