import sqlite3

import pandas as pd

USERNAME = "maxwellholloway" # your mac's username; you can find it through `ls /Users`

conn = sqlite3.connect(f"/Users/{USERNAME}/Library/Messages/chat.db", isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)

query = """
SELECT
    datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime") AS message_date,
    message.text,
    message.is_from_me,
    chat.chat_identifier
FROM
    chat
    JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id
    JOIN message ON chat_message_join.message_id = message. "ROWID"
ORDER BY
    message_date ASC;
"""

db_df = pd.read_sql_query(query, conn)

db_df.to_csv("data/chat.csv", index=False)


