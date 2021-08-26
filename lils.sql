DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS emploers;
DROP TABLE IF EXISTS forms;

PRAGMA foreign_keys=on;

CREATE TABLE forms(
    form_id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_form TEXT NOT NULL,
    long_form TEXT NOT NULL
);

CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    company_inn INTEGER NOT NULL,
    company_form INTEGER NOT NULL,
    FOREIGN KEY (company_form) REFERENCES forms(form_id)
);

CREATE TABLE emploers (
    emploer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    emploer_name TEXT NOT NULL,
    emploer_surname TEXT NOT NULL,
    emploer_patronymic TEXT
);

CREATE TABLE answers (
    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    answer_number TEXT NOT NULL,
    answer_date DATE,
    company INTEGER NOT NULL,
    emploer INTEGER NOT NULL,
    FOREIGN KEY (company) REFERENCES companies(company_id)
    FOREIGN KEY (emploer) REFERENCES emploers(emploer_id)
);
