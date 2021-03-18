-- Volcando estructura para tabla flask_mvc.productos

CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `precio_venta` varchar(255) NOT NULL,
  `precio_compra` varchar(255) NOT NULL,
  `ganancia` int(11) NOT NULL,
  `estado` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla flask_mvc.productos: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `nombre`, `descripcion`, `precio_venta`, `precio_compra`, `ganancia`, `estado`) VALUES
	(1, 'jabones', 'liquido', '6000', '3000', 100, 'Inactivo'),
	(2, 'cepillo ', 'de ropa', '4600', '2300', 100, 'Activo'),
	(3, 'cepillo ', 'de lavar ropa', '4900', '3500', 40, 'Activo'),
	(4, 'leche', 'liquida', '2800', '1400', 100, 'Inactivo'),
	(5, 'fideos', 'sopa', '2000', '1300', 0, 'Activo'),
	(6, 'vive 100', 'energizante sabor a guaraná ', '2000', '1800', 0, 'Inactivo'),
	(7, 'arroz ', ' Integral es un alimento completo', '3900', '3000', 30, 'Activo'),
	(8, 'shampoo', 'anti caída del cabello ', '39000', '30000', 30, 'Activo'),
	(9, 'jabonn', 'blanco ', '2000', '1000', 100, 'Activo'),
	(10, 'atun ', 'capaz ', '2000', '1000', 100, 'Inactivo');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
