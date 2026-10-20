use Academy;

-- Порядок заполнения из задания идет раньше, чем появляются родительские записи
-- (оценки и предметы ссылаются на студентов и преподавателей), поэтому
-- на время вставки проверка внешних ключей отключена.
set foreign_key_checks = 0;

-- 1. Сначала: classes, student_group, student_grades, subjects

insert into classes (class_name, places) values
    ('Аудитория 101', 30),
    ('Аудитория 102', 28),
    ('Лаборатория 201', 20),
    ('Лаборатория 202', 20),
    ('Актовый зал', 100),
    ('Спортзал', 60);

insert into student_group (group_name, stud_count, speciality) values
    ('РПО-25-1', 24, 'Разработка программного обеспечения'),
    ('РПО-25-2', 22, 'Разработка программного обеспечения'),
    ('СА-25-1', 20, 'Системное администрирование');

insert into student_grades (student_id, subject_id, grade, grade_date) values
    (1, 1, 5, '2026-09-15'),
    (2, 1, 4, '2026-09-15'),
    (3, 1, 5, '2026-09-16'),
    (4, 2, 4, '2026-09-17'),
    (5, 2, 3, '2026-09-17'),
    (6, 2, 5, '2026-09-18'),
    (7, 3, 4, '2026-09-22'),
    (8, 3, 5, '2026-09-22'),
    (9, 3, 4, '2026-09-23'),
    (1, 2, 5, '2026-09-24'),
    (2, 3, 4, '2026-09-25'),
    (4, 1, 3, '2026-09-26');

insert into subjects (sub_name, hours, teacher_id) values
    ('Программирование на Python', 120, 1),
    ('Базы данных', 96, 2),
    ('Операционные системы', 80, 3),
    ('Компьютерные сети', 72, 3),
    ('Основы алгоритмизации', 64, 1),
    ('Английский язык для IT', 48, 4);

-- 2. После: teachers, students, lessons, shedules

insert into teachers (full_name, email, phone) values
    ('Иванов Пётр Сергеевич', 'ivanov.ps@academy.ru', '+7-900-111-11-01'),
    ('Смирнова Анна Викторовна', 'smirnova.av@academy.ru', '+7-900-111-11-02'),
    ('Кузнецов Дмитрий Олегович', 'kuznetsov.do@academy.ru', '+7-900-111-11-03'),
    ('Орлова Мария Андреевна', 'orlova.ma@academy.ru', '+7-900-111-11-04');

insert into students (full_name, email, phone, birthday_date, created_at, student_group_id) values
    ('Белов Артём Игоревич', 'belov.ai@student.ru', '+7-911-000-00-01', '2008-03-12', '2025-09-01', 1),
    ('Волкова Дарья Павловна', 'volkova.dp@student.ru', '+7-911-000-00-02', '2008-07-25', '2025-09-01', 1),
    ('Громов Никита Андреевич', 'gromov.na@student.ru', '+7-911-000-00-03', '2007-11-02', '2025-09-01', 1),
    ('Дмитриева Алина Сергеевна', 'dmitrieva.as@student.ru', '+7-911-000-00-04', '2008-01-30', '2025-09-01', 2),
    ('Егоров Максим Олегович', 'egorov.mo@student.ru', '+7-911-000-00-05', '2008-05-18', '2025-09-01', 2),
    ('Жукова Елена Ильинична', 'zhukova.ei@student.ru', '+7-911-000-00-06', '2007-12-09', '2025-09-01', 2),
    ('Зайцев Кирилл Денисович', 'zaytsev.kd@student.ru', '+7-911-000-00-07', '2008-09-14', '2025-09-01', 3),
    ('Иванова Софья Романовна', 'ivanova.sr@student.ru', '+7-911-000-00-08', '2008-04-03', '2025-09-01', 3),
    ('Козлов Тимур Артёмович', 'kozlov.ta@student.ru', '+7-911-000-00-09', '2007-10-21', '2025-09-01', 3);

insert into lessons (theme_name, stud_count, subject_id, student_group_id, teacher_id, class_id) values
    ('Переменные и типы данных', 24, 1, 1, 1, 3),
    ('Проектирование таблиц', 22, 2, 2, 2, 4),
    ('Процессы и потоки', 20, 3, 3, 3, 1),
    ('Модель OSI', 20, 4, 3, 3, 2),
    ('Алгоритмы сортировки', 24, 5, 1, 1, 1),
    ('Present Simple', 22, 6, 2, 4, 2);

insert into shedules (date_day, lesson_1_id, lesson_2_id, lesson_3_id, lesson_4_id, lesson_5_id, lesson_6_id, lesson_7_id, lesson_8_id, created_at) values
    ('2026-10-26', 1, 5, 3, 4, null, null, null, null, '2026-10-20'),
    ('2026-10-27', 2, 6, null, null, null, null, null, null, '2026-10-20'),
    ('2026-10-28', 3, 4, 1, 5, null, null, null, null, '2026-10-20');

set foreign_key_checks = 1;

-- 3. Запрос в конце скрипта: расписание, где видно данные из всех таблиц

select
    s.date_day as day,
    l.theme_name as lesson,
    sub.sub_name as subject,
    g.group_name as student_group,
    t.full_name as teacher,
    c.class_name as class_room
from shedules s
join lessons l on l.id = s.lesson_1_id
join subjects sub on sub.id = l.subject_id
join student_group g on g.id = l.student_group_id
join teachers t on t.id = l.teacher_id
join classes c on c.id = l.class_id
order by s.date_day;
