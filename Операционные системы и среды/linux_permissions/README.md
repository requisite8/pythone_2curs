# Права доступа в Linux (WSL, Ubuntu)

Домашнее задание: создать каталоги и файлы с заданными правами. Команды выполнены в WSL (Ubuntu 26.04), домашняя папка `/home/arsen`.

## Что требовалось

1. Каталог `global_prog` с правами `rwxrw-r--` (764).
2. В нем каталог `my_proj` с правами `rwx------` (700).
3. В `my_proj` два файла с любыми правами.
4. В `global_prog` два файла: первый с правами `rwxrw----` (760), второй с `rwxr--r--` (744).

## История команд и результат

```
$ mkdir global_prog
$ chmod 764 global_prog
$ ls -ld global_prog
drwxrw-r-- 2 arsen arsen 4096 Oct 20 08:24 global_prog
$ mkdir global_prog/my_proj
$ chmod 700 global_prog/my_proj
$ ls -ld global_prog/my_proj
drwx------ 2 arsen arsen 4096 Oct 20 08:24 global_prog/my_proj
$ touch global_prog/my_proj/file1.txt global_prog/my_proj/file2.txt
$ chmod 600 global_prog/my_proj/file2.txt
$ ls -l global_prog/my_proj
total 0
-rw-r--r-- 1 arsen arsen 0 Oct 20 08:24 file1.txt
-rw------- 1 arsen arsen 0 Oct 20 08:24 file2.txt
$ touch global_prog/file_a.txt global_prog/file_b.txt
$ chmod 760 global_prog/file_a.txt
$ chmod 744 global_prog/file_b.txt
$ ls -l global_prog
total 4
-rwxrw---- 1 arsen arsen    0 Oct 20 08:24 file_a.txt
-rwxr--r-- 1 arsen arsen    0 Oct 20 08:24 file_b.txt
drwx------ 2 arsen arsen 4096 Oct 20 08:24 my_proj
```

## Как читать права

| Цифры | Запись | Владелец | Группа | Остальные |
|-------|--------|----------|--------|-----------|
| 764 | rwxrw-r-- | rwx | rw- | r-- |
| 700 | rwx------ | rwx | --- | --- |
| 760 | rwxrw---- | rwx | rw- | --- |
| 744 | rwxr--r-- | rwx | r-- | r-- |

Права считаются как r=4, w=2, x=1 для каждого из трех классов (владелец, группа, остальные).
