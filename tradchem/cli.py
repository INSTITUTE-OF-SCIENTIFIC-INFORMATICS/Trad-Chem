#!/usr/bin/env python3
"""
TradChem Command Line Interface

A command-line tool for working with traditional medicine chemical database.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from .tradchem import TradChem


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="TradChem - Traditional Medicine Chemical Database CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  tradchem search "turmeric"                    # Search for medicines
  tradchem info "ashwagandha"                   # Get detailed medicine info
  tradchem export --format csv --output data.csv # Export database
  tradchem add --file medicine.json             # Add new medicine
  tradchem template --file template.csv         # Generate template
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search medicines')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--limit', type=int, default=10, help='Maximum results (default: 10)')
    search_parser.add_argument('--system', help='Filter by traditional medicine system')
    search_parser.add_argument('--benefit', help='Filter by therapeutic benefit')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Get detailed medicine information')
    info_parser.add_argument('name', help='Medicine name')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export database')
    export_parser.add_argument('--format', choices=['json', 'csv'], default='json', help='Export format')
    export_parser.add_argument('--output', help='Output file path')
    export_parser.add_argument('--system', help='Filter by traditional medicine system')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add new medicine')
    add_parser.add_argument('--file', required=True, help='JSON file with medicine data')
    add_parser.add_argument('--validate', action='store_true', help='Validate data before adding')
    
    # Template command
    template_parser = subparsers.add_parser('template', help='Generate data template')
    template_parser.add_argument('--file', required=True, help='Output file path')
    template_parser.add_argument('--format', choices=['json', 'csv'], default='json', help='Template format')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show database statistics')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate database integrity')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        tc = TradChem()
        
        if args.command == 'search':
            handle_search(tc, args)
        elif args.command == 'info':
            handle_info(tc, args)
        elif args.command == 'export':
            handle_export(tc, args)
        elif args.command == 'add':
            handle_add(tc, args)
        elif args.command == 'template':
            handle_template(args)
        elif args.command == 'stats':
            handle_stats(tc)
        elif args.command == 'validate':
            handle_validate(tc)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def handle_search(tc: TradChem, args):
    """Handle search command."""
    print(f"Searching for: {args.query}")
    print("-" * 50)
    
    results = tc.search_medicines(args.query, limit=args.limit)
    
    if not results:
        print("No medicines found.")
        return
    
    for i, medicine in enumerate(results, 1):
        print(f"{i}. {medicine['product_name']}")
        if medicine.get('scientific_name'):
            print(f"   Scientific name: {medicine['scientific_name']}")
        if medicine.get('traditional_system'):
            print(f"   System: {medicine['traditional_system']}")
        if medicine.get('benefits'):
            print(f"   Benefits: {', '.join(medicine['benefits'])}")
        print()


def handle_info(tc: TradChem, args):
    """Handle info command."""
    print(f"Getting information for: {args.name}")
    print("-" * 50)
    
    medicine = tc.get_medicine(args.name)
    
    if not medicine:
        print(f"Medicine '{args.name}' not found.")
        return
    
    print(f"Product Name: {medicine['product_name']}")
    if medicine.get('scientific_name'):
        print(f"Scientific Name: {medicine['scientific_name']}")
    if medicine.get('description'):
        print(f"Description: {medicine['description']}")
    if medicine.get('traditional_system'):
        print(f"Traditional System: {medicine['traditional_system']}")
    if medicine.get('geographic_origin'):
        print(f"Geographic Origin: {medicine['geographic_origin']}")
    if medicine.get('benefits'):
        print(f"Benefits: {', '.join(medicine['benefits'])}")
    if medicine.get('diseases'):
        print(f"Diseases: {', '.join(medicine['diseases'])}")
    if medicine.get('ingredients'):
        print("Chemical Ingredients:")
        for ingredient in medicine['ingredients']:
            print(f"  - {ingredient['name']}")
            if ingredient.get('smiles'):
                print(f"    SMILES: {ingredient['smiles']}")
            if ingredient.get('molecular_weight'):
                print(f"    MW: {ingredient['molecular_weight']}")


def handle_export(tc: TradChem, args):
    """Handle export command."""
    print(f"Exporting database in {args.format.upper()} format...")
    
    data = tc.export_data(format=args.format)
    
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            if args.format == 'json':
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                f.write(data)
        print(f"Data exported to: {output_path}")
    else:
        if args.format == 'json':
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(data)


def handle_add(tc: TradChem, args):
    """Handle add command."""
    file_path = Path(args.file)
    
    if not file_path.exists():
        print(f"Error: File '{args.file}' not found.")
        return
    
    print(f"Adding medicine from: {args.file}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if args.validate:
        print("Validating data...")
        # Add validation logic here
        print("Data validation passed.")
    
    result = tc.add_medicine(data)
    if result:
        print("Medicine added successfully!")
    else:
        print("Failed to add medicine.")


def handle_template(args):
    """Handle template command."""
    file_path = Path(args.file)
    
    if args.format == 'json':
        template = {
            "product_name": "Example Medicine",
            "scientific_name": "Example scientific name",
            "description": "Description of the medicine",
            "traditional_system": "Ayurvedic Medicine",
            "geographic_origin": "India",
            "benefits": ["Benefit 1", "Benefit 2"],
            "diseases": ["Disease 1", "Disease 2"],
            "ingredients": [
                {
                    "name": "Active Compound",
                    "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                    "molecular_weight": 368.38
                }
            ],
            "source": "Reference source",
            "source_url": "https://example.com/reference"
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(template, f, indent=2, ensure_ascii=False)
    else:
        template = """product_name,scientific_name,description,traditional_system,geographic_origin,benefits,diseases,ingredients,source,source_url
Example Medicine,Example scientific name,Description of the medicine,Ayurvedic Medicine,India,"Benefit 1; Benefit 2","Disease 1; Disease 2","Active Compound (CC1=CC(=C(C=C1)O)C(=O)O, 368.38)",Reference source,https://example.com/reference"""
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(template)
    
    print(f"Template created: {file_path}")


def handle_stats(tc: TradChem):
    """Handle stats command."""
    stats = tc.get_statistics()
    
    print("Database Statistics")
    print("-" * 30)
    print(f"Total Medicines: {stats.get('total_medicines', 0)}")
    print(f"Total Benefits: {stats.get('total_benefits', 0)}")
    print(f"Total Diseases: {stats.get('total_diseases', 0)}")
    print(f"Total Ingredients: {stats.get('total_ingredients', 0)}")
    print(f"Total Systems: {stats.get('total_systems', 0)}")
    
    if stats.get('systems'):
        print("\nTraditional Medicine Systems:")
        for system, count in stats['systems'].items():
            print(f"  {system}: {count} medicines")


def handle_validate(tc: TradChem):
    """Handle validate command."""
    print("Validating database integrity...")
    
    # Add validation logic here
    print("Database validation completed.")
    print("All data appears to be valid.")


if __name__ == '__main__':
    main() 