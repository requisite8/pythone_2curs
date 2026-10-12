-- YouTube: схема для SQLite (только колонки PK и FK)
PRAGMA foreign_keys = ON;

-- Справочники

CREATE TABLE countries (
    id INTEGER PRIMARY KEY
);

CREATE TABLE languages (
    id INTEGER PRIMARY KEY
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY
);

CREATE TABLE currencies (
    id INTEGER PRIMARY KEY
);

CREATE TABLE tags (
    id INTEGER PRIMARY KEY
);

CREATE TABLE report_reasons (
    id INTEGER PRIMARY KEY
);

-- Пользователи и каналы

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries (id)
);

CREATE TABLE channels (
    id INTEGER PRIMARY KEY,
    owner_user_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (owner_user_id) REFERENCES users (id),
    FOREIGN KEY (country_id) REFERENCES countries (id)
);

CREATE TABLE subscriptions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    channel_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (channel_id) REFERENCES channels (id)
);

CREATE TABLE membership_levels (
    id INTEGER PRIMARY KEY,
    channel_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    FOREIGN KEY (channel_id) REFERENCES channels (id),
    FOREIGN KEY (currency_id) REFERENCES currencies (id)
);

CREATE TABLE memberships (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    membership_level_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (membership_level_id) REFERENCES membership_levels (id)
);

-- Видео

CREATE TABLE videos (
    id INTEGER PRIMARY KEY,
    channel_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    FOREIGN KEY (channel_id) REFERENCES channels (id),
    FOREIGN KEY (category_id) REFERENCES categories (id),
    FOREIGN KEY (language_id) REFERENCES languages (id)
);

CREATE TABLE video_tags (
    id INTEGER PRIMARY KEY,
    video_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY (video_id) REFERENCES videos (id),
    FOREIGN KEY (tag_id) REFERENCES tags (id)
);

CREATE TABLE subtitles (
    id INTEGER PRIMARY KEY,
    video_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    FOREIGN KEY (video_id) REFERENCES videos (id),
    FOREIGN KEY (language_id) REFERENCES languages (id)
);

CREATE TABLE thumbnails (
    id INTEGER PRIMARY KEY,
    video_id INTEGER NOT NULL,
    FOREIGN KEY (video_id) REFERENCES videos (id)
);

CREATE TABLE video_likes (
    id INTEGER PRIMARY KEY,
    video_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (video_id) REFERENCES videos (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE watch_history (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    video_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (video_id) REFERENCES videos (id)
);

-- Плейлисты

CREATE TABLE playlists (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    channel_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (channel_id) REFERENCES channels (id)
);

CREATE TABLE playlist_videos (
    id INTEGER PRIMARY KEY,
    playlist_id INTEGER NOT NULL,
    video_id INTEGER NOT NULL,
    FOREIGN KEY (playlist_id) REFERENCES playlists (id),
    FOREIGN KEY (video_id) REFERENCES videos (id)
);

-- Комментарии

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    video_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    parent_comment_id INTEGER,
    FOREIGN KEY (video_id) REFERENCES videos (id),
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (parent_comment_id) REFERENCES comments (id)
);

CREATE TABLE comment_likes (
    id INTEGER PRIMARY KEY,
    comment_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (comment_id) REFERENCES comments (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Прямые эфиры

CREATE TABLE live_streams (
    id INTEGER PRIMARY KEY,
    channel_id INTEGER NOT NULL,
    video_id INTEGER NOT NULL,
    FOREIGN KEY (channel_id) REFERENCES channels (id),
    FOREIGN KEY (video_id) REFERENCES videos (id)
);

CREATE TABLE chat_messages (
    id INTEGER PRIMARY KEY,
    live_stream_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (live_stream_id) REFERENCES live_streams (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE super_chats (
    id INTEGER PRIMARY KEY,
    chat_message_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    FOREIGN KEY (chat_message_id) REFERENCES chat_messages (id),
    FOREIGN KEY (currency_id) REFERENCES currencies (id)
);

-- Реклама

CREATE TABLE advertisers (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE ads (
    id INTEGER PRIMARY KEY,
    advertiser_id INTEGER NOT NULL,
    video_id INTEGER NOT NULL,
    FOREIGN KEY (advertiser_id) REFERENCES advertisers (id),
    FOREIGN KEY (video_id) REFERENCES videos (id)
);

-- Уведомления и жалобы

CREATE TABLE notifications (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    video_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (video_id) REFERENCES videos (id)
);

CREATE TABLE reports (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    video_id INTEGER NOT NULL,
    report_reason_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (video_id) REFERENCES videos (id),
    FOREIGN KEY (report_reason_id) REFERENCES report_reasons (id)
);
