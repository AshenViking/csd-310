/*
whatabook
Carl Young
2/19/2022
*/

-- creates database
CREATE DATABASE whatabook;

-- user drop test
Drop USER IF EXISTS 'whatabook_user'@'localhost';

-- create user and add privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- database privileges to created user
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- key drop test got to love stack overflow for examples 
-- since the ORD had foreign keys thats what is going to be droped if it exists
ALTER TABLE whatabook DROP FOREIGN KEY fk_user;
ALTER TABLE whatabook DROP FOREIGN KEY fk_book;

-- table drop test
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;

-- creating tables yay
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);    

CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(wishlist_id)
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id)
);



-- store record insert
INSERT INTO store(locale)
    VALUES('1100 Franklin St, Phoenix, AZ 85001');



-- book records insert
INSERT INTO book(book_name, author)
    VALUES('Absalom, Absalom!', 'William Faulkner');

INSERT INTO book(book_name, author)
    VALUES('A Time to Kill', 'John Grisham');

INSERT INTO book(book_name, author)
    VALUES('The House of Mirth', 'Edith Wharton');

INSERT INTO book(book_name, author)
    VALUES('East of Eden', 'John Steinbeck');

INSERT INTO book(book_name, author)
    VALUES('The Sun Also Rises', 'Ernest Hemingway');

INSERT INTO book(book_name, author)
    VALUES('Number of the Stars', 'Lois Lowry');

INSERT INTO book(book_name, author)
    VALUES('Brave New World', 'Aldous Huxley');

INSERT INTO book(book_name, author)
    VALUES('Rosemary and Rue', 'Seanan McGuire');

INSERT INTO book(book_name, author)
    VALUES('The Fault In Our Stars', 'John Green');

INSERT INTO book(book_name, author)
    VALUES('Cold Comfort Farm', 'Stella Gibbons');



-- user inserts
-- random name generators are nice
INSERT INTO user(first_name, last_name)
    VALUES('Guqil', 'Mal');

INSERT INTO user(first_name, last_name)
    VALUES('Argan', 'Saahish');

INSERT INTO user(first_name, last_name)
    VALUES('Cagduz', 'Zas');


-- wishlist inserts
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name='Guqil'),
        (SELECT book_id FROM book WHERE book_name='The Fault In Our Stars')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name='Argan'),
        (SELECT book_id FROM book WHERE book_name='Rosemary and Rue')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name='Cagduz'),
        (SELECT book_id FROM book WHERE book_name='Brave New World')
    );