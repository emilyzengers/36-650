CREATE TABLE new_table(
    player INTEGER REFERENCES more_player_stats,
    pr1 NUMERIC,
    position TEXT
)

INSERT INTO new_table (player, pr1) 
    (SELECT id, round(per - 67*va/(gp*minutes),1) 
    from more_player_stats); 

UPDATE new_table
set position = 'PF'
where pr1 >= 11.3;

UPDATE new_table
set position = 'PG' 
where pr1 >= 10.8 and pr1 < 11.3;

UPDATE new_table
set position = 'C'
where pr1 >= 10.6 and pr1 < 10.8;

UPDATE new_table 
set position = 'SG/SF'
where pr1 >= 0 and pr1 < 10.6;

SELECT * from new_table LIMIT 10;