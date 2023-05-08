create table users(
    user_id varchar(36) primary key,
    created_at datetime not null
);

create table questions(
    question_id varchar(36) primary key,
    title varchar(255) not null,
    body varchar(255) null,
    answer JSON,
    created_at datetime not null
);
