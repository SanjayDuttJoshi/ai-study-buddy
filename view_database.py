#!/usr/bin/env python3
"""
Database Viewer - Quick tool to view SQLite database contents
Usage: python3 view_database.py
"""

import sqlite3
from pathlib import Path

# Database path
DB_PATH = Path(__file__).parent / "ai_study_buddy.db"

def view_database():
    """View database contents"""
    
    if not DB_PATH.exists():
        print(f"❌ Database not found at: {DB_PATH}")
        print("💡 Run the backend first to create the database")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("📊 AI Study Buddy - Database Viewer")
    print("=" * 60)
    
    # List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print(f"\n📋 Tables in database ({len(tables)} total):")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Show details for each table
    for table in tables:
        table_name = table[0]
        print(f"\n{'='*60}")
        print(f"📊 Table: {table_name}")
        print(f"{'='*60}")
        
        # Table structure
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        print("\n🏗️  Structure:")
        print(f"  {'Column':<20} {'Type':<15} {'Nullable':<10} {'Key'}")
        print(f"  {'-'*20} {'-'*15} {'-'*10} {'-'*10}")
        for col in columns:
            col_id, name, col_type, not_null, default, pk = col
            nullable = "NO" if not_null else "YES"
            key = "PRIMARY" if pk else ""
            print(f"  {name:<20} {col_type:<15} {nullable:<10} {key}")
        
        # Row count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"\n📈 Total rows: {count}")
        
        # Show first 5 rows
        if count > 0:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
            rows = cursor.fetchall()
            
            print(f"\n📄 First {len(rows)} row(s):")
            
            # Column headers
            col_names = [col[1] for col in columns]
            header = "  | ".join(f"{name:<15}" for name in col_names)
            print(f"  {header}")
            print(f"  {'-' * len(header)}")
            
            # Data rows
            for row in rows:
                row_str = "  | ".join(f"{str(val):<15}" for val in row)
                print(f"  {row_str}")
        else:
            print("  (empty table)")
    
    print(f"\n{'='*60}")
    print("✅ Database view complete!")
    print(f"📁 Database location: {DB_PATH}")
    print(f"💾 Database size: {DB_PATH.stat().st_size / 1024:.2f} KB")
    print("=" * 60)
    
    conn.close()


if __name__ == "__main__":
    try:
        view_database()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Make sure the database file exists and is not corrupted")

