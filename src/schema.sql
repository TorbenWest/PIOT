CREATE TABLE IF NOT EXISTS sd_user
(
    id              int AUTO_INCREMENT PRIMARY KEY,
    username        VARCHAR(255) NOT NULL UNIQUE CHECK (length(username) > 3 AND length(username) < 16),
    hashed_password VARCHAR(255) NOT NULL,
    bd_addr         VARCHAR(17)  NOT NULL UNIQUE CHECK (bd_addr REGEXP '([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})'),
    is_activated    boolean      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS sd_user_commands
(
    user_id    int          NOT NULL UNIQUE,
    cmd_open   VARCHAR(255) NOT NULL,
    cmd_close  VARCHAR(255) NOT NULL,
    cmd_lock   VARCHAR(255) NOT NULL,
    cmd_unlock VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES sd_user (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sd_user_interaction_log
(
    user_id       int          NOT NULL UNIQUE,
    command       VARCHAR(255) NOT NULL CHECK (command IN ('cmd_open', 'cmd_close', 'cmd_lock', 'cmd_unlock')),
    cmd_timestamp timestamp    NOT NULL,
    FOREIGN KEY (user_id) REFERENCES sd_user (id) ON DELETE CASCADE
);