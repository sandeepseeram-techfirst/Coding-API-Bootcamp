Something bad has happened.

Airflow is used by many users, and it is very likely that others had similar problems and you can easily find
a solution to your problem.

Consider following these steps:

  * gather the relevant information (detailed logs with errors, reproduction steps, details of your deployment)

  * find similar issues using:
     * GitHub Discussions
     * GitHub Issues
     * Stack Overflow
     * the usual search engine you use on a daily basis

  * if you run Airflow on a Managed Service, consider opening an issue using the service support channels

  * if you tried and have difficulty with diagnosing and fixing the problem yourself, consider creating a bug report.
    Make sure however, to include all relevant details and results of your investigation so far.

Python version: 3.8.10
Airflow version: 2.3.4
Node: localhost
-------------------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: no such column: dag.processor_subdir

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.8/dist-packages/flask/app.py", line 2525, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.8/dist-packages/flask/app.py", line 1822, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.8/dist-packages/flask/app.py", line 1820, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.8/dist-packages/flask/app.py", line 1796, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  File "/usr/local/lib/python3.8/dist-packages/airflow/www/auth.py", line 47, in decorated
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/airflow/www/views.py", line 689, in index
    dags = current_dags.options(joinedload(DagModel.tags)).offset(start).limit(dags_per_page).all()
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/orm/query.py", line 2772, in all
    return self._iter().all()
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/orm/query.py", line 2915, in _iter
    result = self.session.execute(
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/orm/session.py", line 1714, in execute
    result = conn._execute_20(statement, params or {}, execution_options)
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/base.py", line 1705, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/sql/elements.py", line 334, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/base.py", line 1572, in _execute_clauseelement
    ret = self._execute_context(
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/base.py", line 1943, in _execute_context
    self._handle_dbapi_exception(
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/base.py", line 2124, in _handle_dbapi_exception
    util.raise_(
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/util/compat.py", line 210, in raise_
    raise exception
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/usr/local/lib/python3.8/dist-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such column: dag.processor_subdir
[SQL: SELECT anon_1.dag_dag_id AS anon_1_dag_dag_id, anon_1.dag_root_dag_id AS anon_1_dag_root_dag_id, anon_1.dag_is_paused AS anon_1_dag_is_paused, anon_1.dag_is_subdag AS anon_1_dag_is_subdag, anon_1.dag_is_active AS anon_1_dag_is_active, anon_1.dag_last_parsed_time AS anon_1_dag_last_parsed_time, anon_1.dag_last_pickled AS anon_1_dag_last_pickled, anon_1.dag_last_expired AS anon_1_dag_last_expired, anon_1.dag_scheduler_lock AS anon_1_dag_scheduler_lock, anon_1.dag_pickle_id AS anon_1_dag_pickle_id, anon_1.dag_fileloc AS anon_1_dag_fileloc, anon_1.dag_processor_subdir AS anon_1_dag_processor_subdir, anon_1.dag_owners AS anon_1_dag_owners, anon_1.dag_description AS anon_1_dag_description, anon_1.dag_default_view AS anon_1_dag_default_view, anon_1.dag_schedule_interval AS anon_1_dag_schedule_interval, anon_1.dag_timetable_description AS anon_1_dag_timetable_description, anon_1.dag_max_active_tasks AS anon_1_dag_max_active_tasks, anon_1.dag_max_active_runs AS anon_1_dag_max_active_runs, anon_1.dag_has_task_concurrency_limits AS anon_1_dag_has_task_concurrency_limits, anon_1.dag_has_import_errors AS anon_1_dag_has_import_errors, anon_1.dag_next_dagrun AS anon_1_dag_next_dagrun, anon_1.dag_next_dagrun_data_interval_start AS anon_1_dag_next_dagrun_data_interval_start, anon_1.dag_next_dagrun_data_interval_end AS anon_1_dag_next_dagrun_data_interval_end, anon_1.dag_next_dagrun_create_after AS anon_1_dag_next_dagrun_create_after, dag_tag_1.name AS dag_tag_1_name, dag_tag_1.dag_id AS dag_tag_1_dag_id 
FROM (SELECT dag.dag_id AS dag_dag_id, dag.root_dag_id AS dag_root_dag_id, dag.is_paused AS dag_is_paused, dag.is_subdag AS dag_is_subdag, dag.is_active AS dag_is_active, dag.last_parsed_time AS dag_last_parsed_time, dag.last_pickled AS dag_last_pickled, dag.last_expired AS dag_last_expired, dag.scheduler_lock AS dag_scheduler_lock, dag.pickle_id AS dag_pickle_id, dag.fileloc AS dag_fileloc, dag.processor_subdir AS dag_processor_subdir, dag.owners AS dag_owners, dag.description AS dag_description, dag.default_view AS dag_default_view, dag.schedule_interval AS dag_schedule_interval, dag.timetable_description AS dag_timetable_description, dag.max_active_tasks AS dag_max_active_tasks, dag.max_active_runs AS dag_max_active_runs, dag.has_task_concurrency_limits AS dag_has_task_concurrency_limits, dag.has_import_errors AS dag_has_import_errors, dag.next_dagrun AS dag_next_dagrun, dag.next_dagrun_data_interval_start AS dag_next_dagrun_data_interval_start, dag.next_dagrun_data_interval_end AS dag_next_dagrun_data_interval_end, dag.next_dagrun_create_after AS dag_next_dagrun_create_after 
FROM dag 
WHERE dag.is_subdag = 0 AND dag.is_active = 1 AND dag.dag_id IN (SELECT 1 FROM (SELECT 1) WHERE 1!=1) ORDER BY dag.dag_id
 LIMIT ? OFFSET ?) AS anon_1 LEFT OUTER JOIN dag_tag AS dag_tag_1 ON anon_1.dag_dag_id = dag_tag_1.dag_id ORDER BY anon_1.dag_dag_id]
[parameters: (100, 0)]
(Background on this error at: https://sqlalche.me/e/14/e3q8)