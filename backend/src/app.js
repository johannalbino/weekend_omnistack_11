const express = require('express');
const routes = require('./routes');
const cors = require('cors');
const { errors} = require('celebrate');

const app = express();

/**
 * Rota/Recurso
*/

/**
  * Métodos HTTP:
  * 
  * GET: Buscar uma informação do back-end
  * POST: Criar uma informação no back-end
  * PUT: Alterar uma informação no back-end
  * DELETE: Deletar uma informação no back-end
*/

/**
 * Tipos de Parametros:
 * 
 * Query Params: Parâmetro enviados na rota após "?" (Filtros, Paginação ...) -> request.query
 * Route Params: Parâmetros utilizados para identificar recursos. -> request.params
 * Request Body: Corpo da requisição, utilizado para criar ou alterar recursos -> request.body
*/

// Informando que estou utilizando json para o corpo das minhas requisições.
app.use(cors());
app.use(express.json());
app.use(routes);
app.use(errors());


module.exports = app;