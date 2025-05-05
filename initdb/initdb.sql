CREATE DATABASE IF NOT EXISTS projeto;

-- Usa o banco criado
USE projeto;

CREATE TABLE IF NOT EXISTS `tb_export` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`codigo_ano` int NOT NULL,
	`codigo_mes` int NOT NULL,
	`codigo_ncm` int NOT NULL,
	`codigo_unidade` int NOT NULL,
	`codigo_pais` int NOT NULL,
	`estado_origem` varchar(255) NOT NULL,
	`codigo_via_transporte` int NOT NULL,
	`codigo_unidade_receita_federal_embarque` int NOT NULL,
	`quantidade_produto` BIGINT NOT NULL,
	`peso_kilo` BIGINT NOT NULL,
	`valor_mercadoria` BIGINT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `tb_import` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`codigo_ano` int NOT NULL,
	`codigo_mes` int NOT NULL,
	`codigo_ncm` int NOT NULL,
	`codigo_unidade` int NOT NULL,
	`codigo_pais` int NOT NULL,
	`estado_destino` varchar(255) NOT NULL,
	`codigo_via_transporte` int NOT NULL,
	`codigo_unidade_receita_federal_desembarque` int NOT NULL,
	`quantidade_produto` BIGINT NOT NULL,
	`peso_kilo` BIGINT NOT NULL,
	`valor_mercadoria` BIGINT NOT NULL,
	`valor_frete` int NOT NULL,
	`valor_seguro` int NOT NULL,
	PRIMARY KEY (`id`)
);
