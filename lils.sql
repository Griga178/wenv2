DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS emploers;
DROP TABLE IF EXISTS answers_emploers_companies;



CREATE TABLE answers (
    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    num TEXT NOT NULL,
    dat DATE
);

CREATE TABLE companies (
    companie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    inn INTEGER NOT NULL,
    form TEXT NOT NULL
);

CREATE TABLE emploers (
    emploer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT,
    birth_day DATE
);

CREATE TABLE answers_emploers_companies (
  answers_id INTEGER,
  emploer_id INTEGER,
  companies_id INTEGER
)
