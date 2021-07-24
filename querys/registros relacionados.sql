/*SELECT u.nombre AS nombre_usuario, r.nombre AS role_usuario 
FROM usuarios u, roles r 
WHERE u.role = r.id;*/

SELECT u.nombre AS nombre_usuario, r.nombre AS role_usuario
FROM usuarios u, roles r
WHERE u.id = 4
AND u.role = r.id;




