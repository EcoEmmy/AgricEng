from app import app, create_tables, seed_database

if __name__ == '__main__':
    try:
        create_tables()
        seed_database()
    except Exception as e:
        print(f"Database initialization error: {e}")

    app.run(host='0.0.0.0', port=5000, debug=True)
