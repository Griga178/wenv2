DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS emploers;
DROP TABLE IF EXISTS forms;

PRAGMA foreign_keys=on;

CREATE TABLE forms(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    small_name TEXT NOT NULL,
    full_name TEXT NOT NULL
);

CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    inn INTEGER NOT NULL,
    form_id INTEGER NOT NULL,
    FOREIGN KEY (form_id) REFERENCES forms(id)
);

CREATE TABLE emploers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT,
    birth_day DATE
);

CREATE TABLE answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num TEXT NOT NULL,
    dat DATE,
    company_id INTEGER NOT NULL,
    emploer_id INTEGER NOT NULL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
    FOREIGN KEY (emploer_id) REFERENCES emploers(id)
);
