# | Method       | What it does                                        |
# | ------------ | --------------------------------------------------- |
# | `add()`      | Track a new object                                  |
# | `commit()`   | Permanently save all pending changes                |
# | `rollback()` | Undo pending changes in the current transaction     |
# | `flush()`    | Send SQL without committing the transaction         |
# | `refresh()`  | Reload object immediately from the database         |
# | `expire()`   | Mark object as stale; reload on next access         |
# | Identity Map | One Python object per database row within a Session |
