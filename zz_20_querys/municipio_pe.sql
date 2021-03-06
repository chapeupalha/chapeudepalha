INSERT INTO core_regiao (id, nome) VALUES (1, 'Norte');
INSERT INTO core_regiao (id, nome) VALUES (2, 'Nordeste');
INSERT INTO core_regiao (id, nome) VALUES (3, 'Sudeste');
INSERT INTO core_regiao (id, nome) VALUES (4, 'Sul');
INSERT INTO core_regiao (id, nome) VALUES (5, 'Centro-Oeste');

INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (12, 12, 'Acre', 'AC', 1);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (27, 27, 'Alagoas', 'AL', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (16, 16, 'Amapá', 'AP', 1);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (13, 13, 'Amazonas', 'AM', 1);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (29, 29, 'Bahia', 'BA', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (23, 23, 'Ceará', 'CE', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (53, 53, 'Distrito Federal', 'DF', 5);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (32, 32, 'Espírito Santo', 'ES', 3);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (52, 52, 'Goiás', 'GO', 5);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (21, 21, 'Maranhão', 'MA', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (51, 51, 'Mato Grosso', 'MT', 5);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (50, 50, 'Mato Grosso do Sul', 'MS', 5);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (31, 31, 'Minas Gerais', 'MG', 3);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (15, 15, 'Pará', 'PA', 1);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (25, 25, 'Paraíba', 'PB', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (41, 41, 'Paraná', 'PR', 4);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (26, 26, 'Pernambuco', 'PE', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (22, 22, 'Piauí', 'PI', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (33, 33, 'Rio de Janeiro', 'RJ', 3);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (24, 24, 'Rio Grande do Norte', 'RN', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (43, 43, 'Rio Grande do Sul', 'RS', 4);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (11, 11, 'Rondônia', 'RO', 1);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (14, 14, 'Roraima', 'RR', 1);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (42, 42, 'Santa Catarina', 'SC', 4);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (35, 35, 'São Paulo', 'SP', 3);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (28, 28, 'Sergipe', 'SE', 2);
INSERT INTO core_estado (id, codigo_uf, nome, uf, regiao_id) values (17, 17, 'Tocantins', 'TO', 1);

INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600054, 2600054, 'Abreu e Lima', 26, 'PE', 'Pernambuco', '-7.90072', '-34.8984');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600104, 2600104, 'Afogados da Ingazeira', 26, 'PE', 'Pernambuco', '-7.74312', '-37.631');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600203, 2600203, 'Afrânio', 26, 'PE', 'Pernambuco', '-8.51136', '-41.0095');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600302, 2600302, 'Agrestina', 26, 'PE', 'Pernambuco', '-8.45966', '-35.9447');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600401, 2600401, 'Água Preta', 26, 'PE', 'Pernambuco', '-8.70609', '-35.5263');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600500, 2600500, 'Águas Belas', 26, 'PE', 'Pernambuco', '-9.11125', '-37.1226');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600609, 2600609, 'Alagoinha', 26, 'PE', 'Pernambuco', '-8.4665', '-36.7788');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600708, 2600708, 'Aliança', 26, 'PE', 'Pernambuco', '-7.60398', '-35.2227');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600807, 2600807, 'Altinho', 26, 'PE', 'Pernambuco', '-8.48482', '-36.0644');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2600906, 2600906, 'Amaraji', 26, 'PE', 'Pernambuco', '-8.37691', '-35.4501');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601003, 2601003, 'Angelim', 26, 'PE', 'Pernambuco', '-8.88429', '-36.2902');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601052, 2601052, 'Araçoiaba', 26, 'PE', 'Pernambuco', '-7.78391', '-35.0809');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601102, 2601102, 'Araripina', 26, 'PE', 'Pernambuco', '-7.57073', '-40.494');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601201, 2601201, 'Arcoverde', 26, 'PE', 'Pernambuco', '-8.41519', '-37.0577');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601300, 2601300, 'Barra de Guabiraba', 26, 'PE', 'Pernambuco', '-8.42075', '-35.6585');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601409, 2601409, 'Barreiros', 26, 'PE', 'Pernambuco', '-8.81605', '-35.1832');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601508, 2601508, 'Belém de Maria', 26, 'PE', 'Pernambuco', '-8.62504', '-35.8335');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601607, 2601607, 'Belém do São Francisco', 26, 'PE', 'Pernambuco', '-8.75046', '-38.9623');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601706, 2601706, 'Belo Jardim', 26, 'PE', 'Pernambuco', '-8.3313', '-36.4258');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601805, 2601805, 'Betânia', 26, 'PE', 'Pernambuco', '-8.26787', '-38.0345');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2601904, 2601904, 'Bezerros', 26, 'PE', 'Pernambuco', '-8.2328', '-35.796');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602001, 2602001, 'Bodocó', 26, 'PE', 'Pernambuco', '-7.77759', '-39.9338');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602100, 2602100, 'Bom Conselho', 26, 'PE', 'Pernambuco', '-9.16919', '-36.6857');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602209, 2602209, 'Bom Jardim', 26, 'PE', 'Pernambuco', '-7.79695', '-35.5784');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602308, 2602308, 'Bonito', 26, 'PE', 'Pernambuco', '-8.47163', '-35.7292');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602407, 2602407, 'Brejão', 26, 'PE', 'Pernambuco', '-9.02915', '-36.566');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602506, 2602506, 'Brejinho', 26, 'PE', 'Pernambuco', '-7.34694', '-37.2865');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602605, 2602605, 'Brejo da Madre de Deus', 26, 'PE', 'Pernambuco', '-8.14933', '-36.3741');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602704, 2602704, 'Buenos Aires', 26, 'PE', 'Pernambuco', '-7.72449', '-35.3182');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602803, 2602803, 'Buíque', 26, 'PE', 'Pernambuco', '-8.61954', '-37.1606');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2602902, 2602902, 'Cabo de Santo Agostinho', 26, 'PE', 'Pernambuco', '-8.28218', '-35.0253');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603009, 2603009, 'Cabrobó', 26, 'PE', 'Pernambuco', '-8.50548', '-39.3094');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603108, 2603108, 'Cachoeirinha', 26, 'PE', 'Pernambuco', '-8.48668', '-36.2402');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603207, 2603207, 'Caetés', 26, 'PE', 'Pernambuco', '-8.7803', '-36.6268');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603306, 2603306, 'Calçado', 26, 'PE', 'Pernambuco', '-8.73108', '-36.3366');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603405, 2603405, 'Calumbi', 26, 'PE', 'Pernambuco', '-7.93551', '-38.1482');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603454, 2603454, 'Camaragibe', 26, 'PE', 'Pernambuco', '-8.02351', '-34.9782');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603504, 2603504, 'Camocim de São Félix', 26, 'PE', 'Pernambuco', '-8.35865', '-35.7653');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603603, 2603603, 'Camutanga', 26, 'PE', 'Pernambuco', '-7.40545', '-35.2664');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603702, 2603702, 'Canhotinho', 26, 'PE', 'Pernambuco', '-8.87652', '-36.1979');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603801, 2603801, 'Capoeiras', 26, 'PE', 'Pernambuco', '-8.73423', '-36.6306');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603900, 2603900, 'Carnaíba', 26, 'PE', 'Pernambuco', '-7.79342', '-37.7946');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2603926, 2603926, 'Carnaubeira da Penha', 26, 'PE', 'Pernambuco', '-8.31799', '-38.7512');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604007, 2604007, 'Carpina', 26, 'PE', 'Pernambuco', '-7.84566', '-35.2514');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604106, 2604106, 'Caruaru', 26, 'PE', 'Pernambuco', '-8.28455', '-35.9699');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604155, 2604155, 'Casinhas', 26, 'PE', 'Pernambuco', '-7.74084', '-35.7206');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604205, 2604205, 'Catende', 26, 'PE', 'Pernambuco', '-8.67509', '-35.7024');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604304, 2604304, 'Cedro', 26, 'PE', 'Pernambuco', '-7.71179', '-39.2367');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604403, 2604403, 'Chã de Alegria', 26, 'PE', 'Pernambuco', '-8.00679', '-35.204');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604502, 2604502, 'Chã Grande', 26, 'PE', 'Pernambuco', '-8.23827', '-35.4571');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604601, 2604601, 'Condado', 26, 'PE', 'Pernambuco', '-7.58787', '-35.0999');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604700, 2604700, 'Correntes', 26, 'PE', 'Pernambuco', '-9.12117', '-36.3244');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604809, 2604809, 'Cortês', 26, 'PE', 'Pernambuco', '-8.47443', '-35.5468');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2604908, 2604908, 'Cumaru', 26, 'PE', 'Pernambuco', '-8.00827', '-35.6957');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605004, 2605004, 'Cupira', 26, 'PE', 'Pernambuco', '-8.62432', '-35.9518');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605103, 2605103, 'Custódia', 26, 'PE', 'Pernambuco', '-8.08546', '-37.6443');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605152, 2605152, 'Dormentes', 26, 'PE', 'Pernambuco', '-8.44116', '-40.7662');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605202, 2605202, 'Escada', 26, 'PE', 'Pernambuco', '-8.35672', '-35.2241');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605301, 2605301, 'Exu', 26, 'PE', 'Pernambuco', '-7.50364', '-39.7238');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605400, 2605400, 'Feira Nova', 26, 'PE', 'Pernambuco', '-7.94704', '-35.3801');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605459, 2605459, 'Fernando de Noronha', 26, 'PE', 'Pernambuco', '-3.8396', '-32.4107');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605509, 2605509, 'Ferreiros', 26, 'PE', 'Pernambuco', '-7.44666', '-35.2373');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605608, 2605608, 'Flores', 26, 'PE', 'Pernambuco', '-7.85842', '-37.9715');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605707, 2605707, 'Floresta', 26, 'PE', 'Pernambuco', '-8.60307', '-38.5687');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605806, 2605806, 'Frei Miguelinho', 26, 'PE', 'Pernambuco', '-7.93918', '-35.9113');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2605905, 2605905, 'Gameleira', 26, 'PE', 'Pernambuco', '-8.5798', '-35.3846');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606002, 2606002, 'Garanhuns', 26, 'PE', 'Pernambuco', '-8.88243', '-36.4966');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606101, 2606101, 'Glória do Goitá', 26, 'PE', 'Pernambuco', '-8.00568', '-35.2904');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606200, 2606200, 'Goiana', 26, 'PE', 'Pernambuco', '-7.5606', '-34.9959');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606309, 2606309, 'Granito', 26, 'PE', 'Pernambuco', '-7.70711', '-39.615');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606408, 2606408, 'Gravatá', 26, 'PE', 'Pernambuco', '-8.21118', '-35.5675');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606507, 2606507, 'Iati', 26, 'PE', 'Pernambuco', '-9.04559', '-36.8498');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606606, 2606606, 'Ibimirim', 26, 'PE', 'Pernambuco', '-8.54026', '-37.7032');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606705, 2606705, 'Ibirajuba', 26, 'PE', 'Pernambuco', '-8.57633', '-36.1812');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606804, 2606804, 'Igarassu', 26, 'PE', 'Pernambuco', '-7.82881', '-34.9013');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2606903, 2606903, 'Iguaracy', 26, 'PE', 'Pernambuco', '-7.83222', '-37.5082');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607604, 2607604, 'Ilha de Itamaracá', 26, 'PE', 'Pernambuco', '-7.74766', '-34.8303');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607000, 2607000, 'Inajá', 26, 'PE', 'Pernambuco', '-8.90206', '-37.8351');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607109, 2607109, 'Ingazeira', 26, 'PE', 'Pernambuco', '-7.66909', '-37.4576');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607208, 2607208, 'Ipojuca', 26, 'PE', 'Pernambuco', '-8.39303', '-35.0609');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607307, 2607307, 'Ipubi', 26, 'PE', 'Pernambuco', '-7.64505', '-40.1476');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607406, 2607406, 'Itacuruba', 26, 'PE', 'Pernambuco', '-8.82231', '-38.6975');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607505, 2607505, 'Itaíba', 26, 'PE', 'Pernambuco', '-8.94569', '-37.4173');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607653, 2607653, 'Itambé', 26, 'PE', 'Pernambuco', '-7.41403', '-35.0963');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607703, 2607703, 'Itapetim', 26, 'PE', 'Pernambuco', '-7.37178', '-37.1863');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607752, 2607752, 'Itapissuma', 26, 'PE', 'Pernambuco', '-7.76798', '-34.8971');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607802, 2607802, 'Itaquitinga', 26, 'PE', 'Pernambuco', '-7.66373', '-35.1002');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607901, 2607901, 'Jaboatão dos Guararapes', 26, 'PE', 'Pernambuco', '-8.11298', '-35.015');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2607950, 2607950, 'Jaqueira', 26, 'PE', 'Pernambuco', '-8.72618', '-35.7942');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608008, 2608008, 'Jataúba', 26, 'PE', 'Pernambuco', '-7.97668', '-36.4943');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608057, 2608057, 'Jatobá', 26, 'PE', 'Pernambuco', '-9.17476', '-38.2607');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608107, 2608107, 'João Alfredo', 26, 'PE', 'Pernambuco', '-7.86565', '-35.5787');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608206, 2608206, 'Joaquim Nabuco', 26, 'PE', 'Pernambuco', '-8.62281', '-35.5288');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608255, 2608255, 'Jucati', 26, 'PE', 'Pernambuco', '-8.70195', '-36.4871');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608305, 2608305, 'Jupi', 26, 'PE', 'Pernambuco', '-8.70904', '-36.4126');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608404, 2608404, 'Jurema', 26, 'PE', 'Pernambuco', '-8.70714', '-36.1347');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608453, 2608453, 'Lagoa do Carro', 26, 'PE', 'Pernambuco', '-7.84383', '-35.3108');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608503, 2608503, 'Lagoa de Itaenga', 26, 'PE', 'Pernambuco', '-7.93005', '-35.2874');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608602, 2608602, 'Lagoa do Ouro', 26, 'PE', 'Pernambuco', '-9.12567', '-36.4584');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608701, 2608701, 'Lagoa dos Gatos', 26, 'PE', 'Pernambuco', '-8.6602', '-35.904');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608750, 2608750, 'Lagoa Grande', 26, 'PE', 'Pernambuco', '-8.99452', '-40.2767');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608800, 2608800, 'Lajedo', 26, 'PE', 'Pernambuco', '-8.65791', '-36.3293');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2608909, 2608909, 'Limoeiro', 26, 'PE', 'Pernambuco', '-7.8726', '-35.4402');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609006, 2609006, 'Macaparana', 26, 'PE', 'Pernambuco', '-7.55564', '-35.4425');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609105, 2609105, 'Machados', 26, 'PE', 'Pernambuco', '-7.68827', '-35.5114');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609154, 2609154, 'Manari', 26, 'PE', 'Pernambuco', '-8.9649', '-37.6313');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609204, 2609204, 'Maraial', 26, 'PE', 'Pernambuco', '-8.79062', '-35.8266');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609303, 2609303, 'Mirandiba', 26, 'PE', 'Pernambuco', '-8.12113', '-38.7388');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614303, 2614303, 'Moreilândia', 26, 'PE', 'Pernambuco', '-7.61931', '-39.546');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609402, 2609402, 'Moreno', 26, 'PE', 'Pernambuco', '-8.10871', '-35.0835');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609501, 2609501, 'Nazaré da Mata', 26, 'PE', 'Pernambuco', '-7.74149', '-35.2193');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609600, 2609600, 'Olinda', 26, 'PE', 'Pernambuco', '-8.01017', '-34.8545');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609709, 2609709, 'Orobó', 26, 'PE', 'Pernambuco', '-7.74553', '-35.5956');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609808, 2609808, 'Orocó', 26, 'PE', 'Pernambuco', '-8.61026', '-39.6026');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2609907, 2609907, 'Ouricuri', 26, 'PE', 'Pernambuco', '-7.87918', '-40.08');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610004, 2610004, 'Palmares', 26, 'PE', 'Pernambuco', '-8.68423', '-35.589');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610103, 2610103, 'Palmeirina', 26, 'PE', 'Pernambuco', '-9.0109', '-36.3242');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610202, 2610202, 'Panelas', 26, 'PE', 'Pernambuco', '-8.66121', '-36.0125');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610301, 2610301, 'Paranatama', 26, 'PE', 'Pernambuco', '-8.91875', '-36.6549');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610400, 2610400, 'Parnamirim', 26, 'PE', 'Pernambuco', '-8.08729', '-39.5795');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610509, 2610509, 'Passira', 26, 'PE', 'Pernambuco', '-7.9971', '-35.5813');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610608, 2610608, 'Paudalho', 26, 'PE', 'Pernambuco', '-7.90287', '-35.1716');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610707, 2610707, 'Paulista', 26, 'PE', 'Pernambuco', '-7.93401', '-34.8684');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610806, 2610806, 'Pedra', 26, 'PE', 'Pernambuco', '-8.49641', '-36.94');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2610905, 2610905, 'Pesqueira', 26, 'PE', 'Pernambuco', '-8.35797', '-36.6978');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611002, 2611002, 'Petrolândia', 26, 'PE', 'Pernambuco', '-9.06863', '-38.3027');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611101, 2611101, 'Petrolina', 26, 'PE', 'Pernambuco', '-9.38866', '-40.5027');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611200, 2611200, 'Poção', 26, 'PE', 'Pernambuco', '-8.18726', '-36.7111');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611309, 2611309, 'Pombos', 26, 'PE', 'Pernambuco', '-8.13982', '-35.3967');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611408, 2611408, 'Primavera', 26, 'PE', 'Pernambuco', '-8.32999', '-35.3544');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611507, 2611507, 'Quipapá', 26, 'PE', 'Pernambuco', '-8.81175', '-36.0137');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611533, 2611533, 'Quixaba', 26, 'PE', 'Pernambuco', '-7.70734', '-37.8446');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611606, 2611606, 'Recife', 26, 'PE', 'Pernambuco', '-8.04666', '-34.8771');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611705, 2611705, 'Riacho das Almas', 26, 'PE', 'Pernambuco', '-8.13742', '-35.8648');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611804, 2611804, 'Ribeirão', 26, 'PE', 'Pernambuco', '-8.50957', '-35.3698');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2611903, 2611903, 'Rio Formoso', 26, 'PE', 'Pernambuco', '-8.6592', '-35.1532');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612000, 2612000, 'Sairé', 26, 'PE', 'Pernambuco', '-8.32864', '-35.6967');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612109, 2612109, 'Salgadinho', 26, 'PE', 'Pernambuco', '-7.9269', '-35.6503');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612208, 2612208, 'Salgueiro', 26, 'PE', 'Pernambuco', '-8.07373', '-39.1247');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612307, 2612307, 'Saloá', 26, 'PE', 'Pernambuco', '-8.9723', '-36.691');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612406, 2612406, 'Sanharó', 26, 'PE', 'Pernambuco', '-8.36097', '-36.5696');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612455, 2612455, 'Santa Cruz', 26, 'PE', 'Pernambuco', '-8.24153', '-40.3434');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612471, 2612471, 'Santa Cruz da Baixa Verde', 26, 'PE', 'Pernambuco', '-7.81339', '-38.1476');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612505, 2612505, 'Santa Cruz do Capibaribe', 26, 'PE', 'Pernambuco', '-7.94802', '-36.2061');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612554, 2612554, 'Santa Filomena', 26, 'PE', 'Pernambuco', '-8.16688', '-40.6079');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612604, 2612604, 'Santa Maria da Boa Vista', 26, 'PE', 'Pernambuco', '-8.79766', '-39.8241');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612703, 2612703, 'Santa Maria do Cambucá', 26, 'PE', 'Pernambuco', '-7.83676', '-35.8941');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612802, 2612802, 'Santa Terezinha', 26, 'PE', 'Pernambuco', '-7.37696', '-37.4787');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2612901, 2612901, 'São Benedito do Sul', 26, 'PE', 'Pernambuco', '-8.8166', '-35.9453');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613008, 2613008, 'São Bento do Una', 26, 'PE', 'Pernambuco', '-8.52637', '-36.4465');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613206, 2613206, 'São João', 26, 'PE', 'Pernambuco', '-8.87576', '-36.3653');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613305, 2613305, 'São Joaquim do Monte', 26, 'PE', 'Pernambuco', '-8.43196', '-35.8035');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613404, 2613404, 'São José da Coroa Grande', 26, 'PE', 'Pernambuco', '-8.88937', '-35.1515');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613503, 2613503, 'São José do Belmonte', 26, 'PE', 'Pernambuco', '-7.85723', '-38.7577');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613602, 2613602, 'São José do Egito', 26, 'PE', 'Pernambuco', '-7.46945', '-37.274');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613701, 2613701, 'São Lourenço da Mata', 26, 'PE', 'Pernambuco', '-8.00684', '-35.0124');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613800, 2613800, 'São Vicente Ferrer', 26, 'PE', 'Pernambuco', '-7.58969', '-35.4808');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613909, 2613909, 'Serra Talhada', 26, 'PE', 'Pernambuco', '-7.98178', '-38.289');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614006, 2614006, 'Serrita', 26, 'PE', 'Pernambuco', '-7.94041', '-39.2951');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614105, 2614105, 'Sertânia', 26, 'PE', 'Pernambuco', '-8.06847', '-37.2684');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614204, 2614204, 'Sirinhaém', 26, 'PE', 'Pernambuco', '-8.58778', '-35.1126');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614402, 2614402, 'Solidão', 26, 'PE', 'Pernambuco', '-7.59472', '-37.6445');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614501, 2614501, 'Surubim', 26, 'PE', 'Pernambuco', '-7.84746', '-35.7481');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614600, 2614600, 'Tabira', 26, 'PE', 'Pernambuco', '-7.58366', '-37.5377');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614709, 2614709, 'Tacaimbó', 26, 'PE', 'Pernambuco', '-8.30867', '-36.3');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614808, 2614808, 'Tacaratu', 26, 'PE', 'Pernambuco', '-9.09798', '-38.1504');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2614857, 2614857, 'Tamandaré', 26, 'PE', 'Pernambuco', '-8.75665', '-35.1033');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615003, 2615003, 'Taquaritinga do Norte', 26, 'PE', 'Pernambuco', '-7.89446', '-36.0423');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615102, 2615102, 'Terezinha', 26, 'PE', 'Pernambuco', '-9.05621', '-36.6272');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615201, 2615201, 'Terra Nova', 26, 'PE', 'Pernambuco', '-8.22244', '-39.3825');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615300, 2615300, 'Timbaúba', 26, 'PE', 'Pernambuco', '-7.50484', '-35.3119');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615409, 2615409, 'Toritama', 26, 'PE', 'Pernambuco', '-8.00955', '-36.0637');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615508, 2615508, 'Tracunhaém', 26, 'PE', 'Pernambuco', '-7.80228', '-35.2314');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615607, 2615607, 'Trindade', 26, 'PE', 'Pernambuco', '-7.759', '-40.2647');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615706, 2615706, 'Triunfo', 26, 'PE', 'Pernambuco', '-7.83272', '-38.0978');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615805, 2615805, 'Tupanatinga', 26, 'PE', 'Pernambuco', '-8.74798', '-37.3445');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2615904, 2615904, 'Tuparetama', 26, 'PE', 'Pernambuco', '-7.6003', '-37.3165');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2616001, 2616001, 'Venturosa', 26, 'PE', 'Pernambuco', '-8.57885', '-36.8742');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2616100, 2616100, 'Verdejante', 26, 'PE', 'Pernambuco', '-7.92235', '-38.9701');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2616183, 2616183, 'Vertente do Lério', 26, 'PE', 'Pernambuco', '-7.77084', '-35.8491');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2616209, 2616209, 'Vertentes', 26, 'PE', 'Pernambuco', '-7.90158', '-35.9681');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2616308, 2616308, 'Vicência', 26, 'PE', 'Pernambuco', '-7.65655', '-35.3139');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2616407, 2616407, 'Vitória de Santo Antão', 26, 'PE', 'Pernambuco', '-8.12819', '-35.2976');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2616506, 2616506, 'Xexéu', 26, 'PE', 'Pernambuco', '-8.8046', '-35.6212');
INSERT INTO core_municipio (id, codigo, nome, estado_id, uf, nome_estado, latitude, longitude) VALUES (2613107, 2613107, 'São Caetano', 26, 'PE', 'Pernambuco', '-8.3376271', '-36.2868983');