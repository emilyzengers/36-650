ALTER TABLE player_bios
ADD COLUMN position TEXT;

UPDATE player_bios
set position = (SELECT position FROM new_table WHERE player = id);

SELECT * from player_bios LIMIT 5;