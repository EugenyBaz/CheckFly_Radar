PRAGMA foreign_keys = ON;

-- =========================================================
-- USERS
-- =========================================================

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    telegram_id INTEGER UNIQUE NOT NULL,
    username TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- AIRPORT GROUPS
-- =========================================================

CREATE TABLE IF NOT EXISTS airport_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL

);

-- =========================================================
-- AIRPORT GROUP MEMBERS
-- =========================================================

CREATE TABLE IF NOT EXISTS airport_group_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    group_code TEXT NOT NULL,
    airport_code TEXT NOT NULL,

    UNIQUE(group_code, airport_code)
);

-- =========================================================
-- SUBSCRIPTIONS
-- =========================================================

CREATE TABLE IF NOT EXISTS subscriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    origin_group TEXT NOT NULL,
    destination_group TEXT NOT NULL,

    allow_moscow_transfer BOOLEAN DEFAULT 1,

    date_from DATE NOT NULL,
    date_to DATE NOT NULL,

    adults INTEGER DEFAULT 1,
    children INTEGER DEFAULT 0,

    baggage_mode TEXT DEFAULT 'checked',

    max_price INTEGER,

    currency TEXT DEFAULT 'RUB',

    status TEXT DEFAULT 'active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)
);

-- =========================================================
-- FLIGHT HISTORY
-- =========================================================

CREATE TABLE IF NOT EXISTS flight_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    subscription_id INTEGER,

    origin TEXT NOT NULL,
    destination TEXT NOT NULL,

    departure_date DATE,
    return_date DATE,

    price INTEGER NOT NULL,
    currency TEXT NOT NULL,

    provider TEXT,

    deep_link TEXT,

    stops INTEGER,

    baggage_included BOOLEAN,

    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(subscription_id) REFERENCES subscriptions(id)
);

-- =========================================================
-- ALERTS SENT
-- =========================================================

CREATE TABLE IF NOT EXISTS alerts_sent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    subscription_id INTEGER NOT NULL,

    flight_hash TEXT NOT NULL,

    sent_price INTEGER,

    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(subscription_id) REFERENCES subscriptions(id)
);

-- =========================================================
-- INDEXES
-- =========================================================

CREATE INDEX IF NOT EXISTS idx_subscriptions_status
ON subscriptions(status);

CREATE INDEX IF NOT EXISTS idx_alerts_hash
ON alerts_sent(flight_hash);

CREATE INDEX IF NOT EXISTS idx_flight_history_subscription
ON flight_history(subscription_id);

CREATE INDEX IF NOT EXISTS idx_users_telegram_id
ON users(telegram_id);


CREATE TABLE IF NOT EXISTS airport_group_aliases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    alias TEXT NOT NULL,
    group_code TEXT NOT NULL,

    UNIQUE(alias, group_code)
)


