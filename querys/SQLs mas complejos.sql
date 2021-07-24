/*SELECT * FROM compra;*/
/*SELECT * FROM producto_compra;*/

/*SELECT p.nombre, p.descripcion, p.precio
FROM producto p
WHERE p.id IN (
	SELECT productoId
	FROM producto_compra pd
	WHERE pd.compraId = 3
);*/

/*SELECT productoId 
FROM producto_compra pd
WHERE pd.compraId = 1;*/