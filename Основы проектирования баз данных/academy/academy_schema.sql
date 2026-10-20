drop schema if exists Academy;
create schema Academy;
use Academy;

-- 1. Сначала: classes, student_group, student_grades, subjects
-- Поля student_id, subject_id и teacher_id уже здесь, а сами FK-связи
-- добавляются ниже командой alter table, когда таблицы students и teachers созданы.

create table classes(
	id int primary key auto_increment,
    class_name varchar(50) not null,
    places tinyint not null
);

create table student_group(
	id int primary key auto_increment,
    group_name varchar(50) not null,
    stud_count tinyint,
    speciality varchar(50) not null
);

create table student_grades(
	id int primary key auto_increment,
    student_id int not null,
    subject_id int not null,
    grade tinyint not null,
    grade_date date
);

create table subjects(
	id int primary key auto_increment,
    sub_name varchar(50) not null,
    hours decimal not null,
    teacher_id int not null
);

-- 2. После: teachers, students, lessons, shedules

create table teachers(
	id int primary key auto_increment,
    full_name varchar(50) not null,
    email varchar(100) unique,
    phone varchar(20) unique
);

create table students(
	id int primary key auto_increment,
    full_name varchar(50) not null,
    email varchar(100) unique,
    phone varchar(20) unique,
    birthday_date date,
    created_at date,
    student_group_id int not null,

    foreign key (student_group_id)
    references student_group(id)
);

create table lessons(
	id int primary key auto_increment,
    theme_name varchar(50) not null,
    stud_count tinyint,
    subject_id int not null,
    student_group_id int not null,
    teacher_id int not null,
    class_id int not null,

    foreign key (subject_id)
    references subjects(id),
    foreign key (student_group_id)
    references student_group(id),
    foreign key (teacher_id)
    references teachers(id),
    foreign key (class_id)
    references classes(id)
);

create table shedules(
	id int primary key auto_increment,
	date_day date not null,
    lesson_1_id int,
    lesson_2_id int,
    lesson_3_id int,
    lesson_4_id int,
    lesson_5_id int,
    lesson_6_id int,
    lesson_7_id int,
    lesson_8_id int,
    created_at date,

    foreign key (lesson_1_id)
    references lessons(id),
    foreign key (lesson_2_id)
    references lessons(id),
    foreign key (lesson_3_id)
    references lessons(id),
    foreign key (lesson_4_id)
    references lessons(id),
    foreign key (lesson_5_id)
    references lessons(id),
    foreign key (lesson_6_id)
    references lessons(id),
    foreign key (lesson_7_id)
    references lessons(id),
    foreign key (lesson_8_id)
    references lessons(id)
);

-- 3. FK для первых таблиц, которые ссылаются на более поздние

alter table subjects
    add constraint fk_subjects_teacher
    foreign key (teacher_id) references teachers(id);

alter table student_grades
    add constraint fk_grades_student
    foreign key (student_id) references students(id),
    add constraint fk_grades_subject
    foreign key (subject_id) references subjects(id);

-- 4. Запрос в конце скрипта: все созданные внешние ключи

select table_name, column_name, referenced_table_name, referenced_column_name
from information_schema.key_column_usage
where table_schema = 'Academy' and referenced_table_name is not null
order by table_name, column_name;
