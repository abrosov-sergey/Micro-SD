Необходимо написать API для отправки уведомлений об изменении статуса Session. Реализуй эндпойнт /session/notify, который будет использовать smtp-сервер, чтобы отправить на заданный адрес электронной почты письмо, что у сессии с конкретным идентификатором новый статус. Идентификатор сессии имеет формат UUID. Status - целое число: 1 - Initial, 2 - Ready, 3 - Running, 4 - Success, 5 - Error. Реализация должна быть на FastAPI.