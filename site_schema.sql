-- DROP TABLE IF EXISTS posts;

-- Комменты
-- первая таблица:
--  AUTO_INCREMENT PRIMARY KEY COMMENT "Идентификатор строки",
-- SERIAL == BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
CREATE TABLE answers (
    answers_id SERIAL PRIMARY KEY COMMENT "Идентификатор ответов",
    num VARCHAR(30) NOT NULL COMMENT "номер ответа м.б. INT",
    dat DATE COMMENT "Дата ответа",
);

CREATE TABLE companies (
    companies_id SERIAL PRIMARY KEY COMMENT "Идентификатор",
    name VARCHAR(100) NOT NULL COMMENT "Название компании",
    inn INT NOT NULL COMMENT "Инн компании",
    form VARCHAR(100) NOT NULL COMMENT "Организационно правовая форма",
);

CREATE TABLE emploers (
    emploer_id SERIAL PRIMARY KEY COMMENT "Идентификатор",
    name VARCHAR(100) NOT NULL COMMENT "Имя пользователя",
    surname VARCHAR(100) NOT NULL COMMENT "Фамилия пользователя",
    patronymic VARCHAR(100) COMMENT "Отчество пользователя",
    birth_day DATE COMMENT "Дата рождения",
);


-- Таблица связи пользователей и ответов и компаний + дата создания
-- Таблица связи пользователей и групп
CREATE TABLE answers_emploers_companies (
  answers_id SERIAL COMMENT "Ссылка на ответ",
  emploer_id SERIAL COMMENT "Ссылка на пользователя",
  companies_id SERIAL COMMENT "Ссылка на компанию",
  PRIMARY KEY (answers_id, emploer_id, companies_id) COMMENT "Составной первичный ключ"
) COMMENT "Связь между ответом и группами";
