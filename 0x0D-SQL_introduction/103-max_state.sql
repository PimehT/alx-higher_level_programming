-- displays the max temperature of each state (ordered by State name).
SELECT MAX(`value`) AS `max_temp`
FROM temperatures
ORDER BY `state`
LIMIT 3;
