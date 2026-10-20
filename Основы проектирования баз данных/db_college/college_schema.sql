create table teachers(
	id int primary key auto_increment,
    full_name varchar(50) not null,
    email varchar(100) unique,
    phone varchar(20) unique
);

create table subjects(
	id int primary key auto_increment,
    sub_name varchar(50) not null,
    hours decimal not null,
    teacher_id int not null,

    foreign key (teacher_id)
    references teachers(id)
);

create table classes(
	id int primary key auto_increment,
    class_name varchar(50) not null,
    places tinyint not null
);

create table student_groups(
	id int primary key auto_increment,
    group_name varchar(50) not null,
    stud_count tinyint,
    speciality varchar(50) not null
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
    references student_groups(id)
);

create table lessons(
	id int primary key auto_increment,
    theme_name varchar(50) not null,
    stud_count tinyint,
    subject_id int not null,
    stud_group_id int not null,
    teacher_id int not null,

    foreign key (subject_id)
    references subjects(id),
    foreign key (stud_group_id)
    references student_groups(id),
    foreign key (teacher_id)
    references teachers(id)
);

create table schedules(
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
