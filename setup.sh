db_name=python scripts/start_database.py
name_and_url=python scripts/start_engine.py
arr=($name_and_url)
engine_name="${arr[0]}"
engine_url="${arr[1]}"

echo "::save-state name=database_name::$db_name"
echo "::set-output name=database_name::$db_name"

echo "::save-state name=engine_name::$engine_name"
echo "::set-output name=engine_name::$engine_name"


echo "::set-output name=engine_url::$engine_url"
