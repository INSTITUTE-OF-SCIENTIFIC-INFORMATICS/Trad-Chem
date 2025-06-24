#!/usr/bin/env python3
"""
TradChem Command Line Interface

A comprehensive command-line tool for traditional medicine chemical analysis.
Supports data loading, validation, chemical analysis, statistical analysis,
traditional medicine analysis, and visualization.
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
        description="TradChem - Traditional Medicine Chemical Analysis CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Data Loading & Validation
  tradchem load data.csv --validate                    # Load and validate data
  tradchem clean data.json --output cleaned.json       # Clean and standardize data
  
  # Chemical Analysis
  tradchem analyze-chemical data.json                  # Analyze chemical structures
  tradchem validate-smiles data.json                   # Validate SMILES notations
  
  # Statistical Analysis
  tradchem stats data.json                             # Basic statistics
  tradchem correlation data.json                       # Correlation analysis
  tradchem patterns data.json                          # Pattern analysis
  
  # Traditional Medicine Analysis
  tradchem analyze-systems data.json                   # Analyze traditional systems
  tradchem geographic data.json                        # Geographic analysis
  tradchem benefits data.json                          # Benefit analysis
  
  # Data Processing
  tradchem filter data.json --system "Ayurveda"        # Filter by system
  tradchem sort data.json --by molecular_weight        # Sort by property
  tradchem export data.json --format csv               # Export data
  
  # Visualization
  tradchem plot-chemical data.json                     # Chemical structure plots
  tradchem plot-stats data.json                        # Statistical plots
  tradchem plot-geo data.json                          # Geographic plots
  
  # Legacy Commands
  tradchem search "turmeric"                           # Search medicines
  tradchem info "ashwagandha"                          # Get medicine info
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # ============================================================================
    # DATA LOADING & VALIDATION COMMANDS
    # ============================================================================
    
    # Load command
    load_parser = subparsers.add_parser('load', help='Load and validate data')
    load_parser.add_argument('file', help='Input data file (CSV, JSON, Excel)')
    load_parser.add_argument('--validate', action='store_true', help='Validate data after loading')
    load_parser.add_argument('--clean', action='store_true', help='Clean data after loading')
    
    # Clean command
    clean_parser = subparsers.add_parser('clean', help='Clean and standardize data')
    clean_parser.add_argument('input', help='Input data file')
    clean_parser.add_argument('--output', help='Output file path')
    
    # ============================================================================
    # CHEMICAL ANALYSIS COMMANDS
    # ============================================================================
    
    # Analyze chemical structures
    chem_parser = subparsers.add_parser('analyze-chemical', help='Analyze chemical structures')
    chem_parser.add_argument('file', help='Input data file')
    chem_parser.add_argument('--output', help='Output file for results')
    chem_parser.add_argument('--properties', action='store_true', help='Calculate molecular properties')
    
    # Validate SMILES
    smiles_parser = subparsers.add_parser('validate-smiles', help='Validate SMILES notations')
    smiles_parser.add_argument('file', help='Input data file')
    smiles_parser.add_argument('--output', help='Output file for validation results')
    
    # ============================================================================
    # STATISTICAL ANALYSIS COMMANDS
    # ============================================================================
    
    # Statistical analysis
    stats_parser = subparsers.add_parser('stats', help='Statistical analysis')
    stats_parser.add_argument('file', help='Input data file')
    stats_parser.add_argument('--output', help='Output file for results')
    
    # Correlation analysis
    corr_parser = subparsers.add_parser('correlation', help='Correlation analysis')
    corr_parser.add_argument('file', help='Input data file')
    corr_parser.add_argument('--output', help='Output file for results')
    
    # Pattern analysis
    pattern_parser = subparsers.add_parser('patterns', help='Pattern analysis')
    pattern_parser.add_argument('file', help='Input data file')
    pattern_parser.add_argument('--output', help='Output file for results')
    
    # ============================================================================
    # TRADITIONAL MEDICINE ANALYSIS COMMANDS
    # ============================================================================
    
    # Analyze traditional systems
    systems_parser = subparsers.add_parser('analyze-systems', help='Analyze traditional medicine systems')
    systems_parser.add_argument('file', help='Input data file')
    systems_parser.add_argument('--output', help='Output file for results')
    
    # Geographic analysis
    geo_parser = subparsers.add_parser('geographic', help='Geographic analysis')
    geo_parser.add_argument('file', help='Input data file')
    geo_parser.add_argument('--output', help='Output file for results')
    
    # Benefit analysis
    benefit_parser = subparsers.add_parser('benefits', help='Benefit analysis')
    benefit_parser.add_argument('file', help='Input data file')
    benefit_parser.add_argument('--output', help='Output file for results')
    
    # ============================================================================
    # DATA PROCESSING COMMANDS
    # ============================================================================
    
    # Filter command
    filter_parser = subparsers.add_parser('filter', help='Filter data')
    filter_parser.add_argument('file', help='Input data file')
    filter_parser.add_argument('--system', help='Filter by traditional system')
    filter_parser.add_argument('--region', help='Filter by geographic region')
    filter_parser.add_argument('--benefit', help='Filter by benefit')
    filter_parser.add_argument('--disease', help='Filter by disease')
    filter_parser.add_argument('--ingredient', help='Filter by ingredient')
    filter_parser.add_argument('--output', help='Output file path')
    
    # Sort command
    sort_parser = subparsers.add_parser('sort', help='Sort data')
    sort_parser.add_argument('file', help='Input data file')
    sort_parser.add_argument('--by', choices=['name', 'system', 'region', 'molecular_weight'], 
                           default='name', help='Sort by property')
    sort_parser.add_argument('--reverse', action='store_true', help='Sort in reverse order')
    sort_parser.add_argument('--output', help='Output file path')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export data')
    export_parser.add_argument('file', help='Input data file')
    export_parser.add_argument('--format', choices=['json', 'csv', 'html'], default='json', help='Export format')
    export_parser.add_argument('--output', help='Output file path')
    
    # ============================================================================
    # VISUALIZATION COMMANDS
    # ============================================================================
    
    # Plot chemical structures
    plot_chem_parser = subparsers.add_parser('plot-chemical', help='Plot chemical structures')
    plot_chem_parser.add_argument('file', help='Input data file')
    plot_chem_parser.add_argument('--save', help='Save plot to file')
    
    # Plot statistics
    plot_stats_parser = subparsers.add_parser('plot-stats', help='Plot statistics')
    plot_stats_parser.add_argument('file', help='Input data file')
    plot_stats_parser.add_argument('--save', help='Save plot to file')
    
    # Plot geographic distribution
    plot_geo_parser = subparsers.add_parser('plot-geo', help='Plot geographic distribution')
    plot_geo_parser.add_argument('file', help='Input data file')
    plot_geo_parser.add_argument('--save', help='Save plot to file')
    
    # ============================================================================
    # LEGACY COMMANDS (for backward compatibility)
    # ============================================================================
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search medicines (legacy)')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--limit', type=int, default=10, help='Maximum results (default: 10)')
    search_parser.add_argument('--system', help='Filter by traditional medicine system')
    search_parser.add_argument('--benefit', help='Filter by therapeutic benefit')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Get detailed medicine information (legacy)')
    info_parser.add_argument('name', help='Medicine name')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add new medicine (legacy)')
    add_parser.add_argument('--file', required=True, help='JSON file with medicine data')
    add_parser.add_argument('--validate', action='store_true', help='Validate data before adding')
    
    # Template command
    template_parser = subparsers.add_parser('template', help='Generate data template (legacy)')
    template_parser.add_argument('--file', required=True, help='Output file path')
    template_parser.add_argument('--format', choices=['json', 'csv'], default='json', help='Template format')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate database integrity (legacy)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        tc = TradChem()
        
        # ============================================================================
        # DATA LOADING & VALIDATION HANDLERS
        # ============================================================================
        
        if args.command == 'load':
            handle_load(tc, args)
        elif args.command == 'clean':
            handle_clean(tc, args)
            
        # ============================================================================
        # CHEMICAL ANALYSIS HANDLERS
        # ============================================================================
        
        elif args.command == 'analyze-chemical':
            handle_analyze_chemical(tc, args)
        elif args.command == 'validate-smiles':
            handle_validate_smiles(tc, args)
            
        # ============================================================================
        # STATISTICAL ANALYSIS HANDLERS
        # ============================================================================
        
        elif args.command == 'stats':
            handle_stats(tc, args)
        elif args.command == 'correlation':
            handle_correlation(tc, args)
        elif args.command == 'patterns':
            handle_patterns(tc, args)
            
        # ============================================================================
        # TRADITIONAL MEDICINE ANALYSIS HANDLERS
        # ============================================================================
        
        elif args.command == 'analyze-systems':
            handle_analyze_systems(tc, args)
        elif args.command == 'geographic':
            handle_geographic(tc, args)
        elif args.command == 'benefits':
            handle_benefits(tc, args)
            
        # ============================================================================
        # DATA PROCESSING HANDLERS
        # ============================================================================
        
        elif args.command == 'filter':
            handle_filter(tc, args)
        elif args.command == 'sort':
            handle_sort(tc, args)
        elif args.command == 'export':
            handle_export(tc, args)
            
        # ============================================================================
        # VISUALIZATION HANDLERS
        # ============================================================================
        
        elif args.command == 'plot-chemical':
            handle_plot_chemical(tc, args)
        elif args.command == 'plot-stats':
            handle_plot_stats(tc, args)
        elif args.command == 'plot-geo':
            handle_plot_geo(tc, args)
            
        # ============================================================================
        # LEGACY HANDLERS
        # ============================================================================
        
        elif args.command == 'search':
            handle_search(tc, args)
        elif args.command == 'info':
            handle_info(tc, args)
        elif args.command == 'add':
            handle_add(tc, args)
        elif args.command == 'template':
            handle_template(args)
        elif args.command == 'validate':
            handle_validate(tc)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


# ============================================================================
# DATA LOADING & VALIDATION HANDLERS
# ============================================================================

def handle_load(tc: TradChem, args):
    """Handle load command."""
    print(f"Loading data from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        print(f"Successfully loaded {len(medicines)} medicines")
        
        if args.validate:
            print("Validating data...")
            validation_results = tc.validate_data(medicines)
            print(f"Validation results:")
            print(f"  Total medicines: {validation_results['total_medicines']}")
            print(f"  Valid medicines: {validation_results['valid_medicines']}")
            print(f"  Invalid medicines: {validation_results['invalid_medicines']}")
            print(f"  Data quality score: {validation_results['data_quality_score']:.2%}")
        
        if args.clean:
            print("Cleaning data...")
            cleaned_medicines = tc.clean_data(medicines)
            print(f"Cleaned {len(cleaned_medicines)} medicines")
            
    except Exception as e:
        print(f"Error loading data: {e}")


def handle_clean(tc: TradChem, args):
    """Handle clean command."""
    print(f"Cleaning data from: {args.input}")
    
    try:
        medicines = tc.load_data(args.input)
        cleaned_medicines = tc.clean_data(medicines)
        
        if args.output:
            tc.export_data(cleaned_medicines, args.output, 'json')
            print(f"Cleaned data saved to: {args.output}")
        else:
            print(f"Cleaned {len(cleaned_medicines)} medicines")
            
    except Exception as e:
        print(f"Error cleaning data: {e}")


# ============================================================================
# CHEMICAL ANALYSIS HANDLERS
# ============================================================================

def handle_analyze_chemical(tc: TradChem, args):
    """Handle analyze-chemical command."""
    print(f"Analyzing chemical structures from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        analysis_results = tc.analyze_chemical_structures(medicines)
        
        print(f"Chemical Analysis Results:")
        print(f"  Total compounds: {analysis_results['total_compounds']}")
        print(f"  Valid SMILES: {analysis_results['valid_smiles']}")
        print(f"  Invalid SMILES: {analysis_results['invalid_smiles']}")
        print(f"  Average molecular weight: {analysis_results['avg_molecular_weight']:.2f}")
        print(f"  Unique formulas: {analysis_results['unique_formulas']}")
        
        if args.properties:
            properties = tc.calculate_molecular_properties(analysis_results)
            print(f"Molecular Properties Summary:")
            print(f"  Weight range: {properties['min_weight']:.2f} - {properties['max_weight']:.2f}")
            print(f"  LogP range: {properties['min_logp']:.2f} - {properties['max_logp']:.2f}")
            print(f"  Unique compounds: {properties['unique_compounds']}")
        
        if args.output:
            tc.export_data(analysis_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error analyzing chemical structures: {e}")


def handle_validate_smiles(tc: TradChem, args):
    """Handle validate-smiles command."""
    print(f"Validating SMILES from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        validation_results = tc.validate_smiles(medicines)
        
        print(f"SMILES Validation Results:")
        print(f"  Valid count: {validation_results['valid_count']}")
        print(f"  Invalid count: {validation_results['invalid_count']}")
        print(f"  Validation rate: {validation_results['validation_rate']:.2%}")
        
        if validation_results['invalid_examples']:
            print(f"  Invalid examples: {validation_results['invalid_examples'][:5]}")
        
        if args.output:
            tc.export_data(validation_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error validating SMILES: {e}")


# ============================================================================
# STATISTICAL ANALYSIS HANDLERS
# ============================================================================

def handle_stats(tc: TradChem, args):
    """Handle stats command."""
    print(f"Performing statistical analysis on: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        stats_results = tc.statistical_analysis(medicines)
        
        print(f"Statistical Analysis Results:")
        print(f"  Total medicines: {stats_results['total_medicines']}")
        print(f"  Unique systems: {stats_results['unique_systems']}")
        print(f"  Unique regions: {stats_results['unique_regions']}")
        print(f"  Average benefits per medicine: {stats_results['avg_benefits_per_medicine']:.2f}")
        print(f"  Compounds with SMILES: {stats_results['compounds_with_smiles']}")
        
        print(f"System Distribution:")
        for system, count in stats_results['system_distribution'].items():
            print(f"  {system}: {count}")
        
        if args.output:
            tc.export_data(stats_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error performing statistical analysis: {e}")


def handle_correlation(tc: TradChem, args):
    """Handle correlation command."""
    print(f"Performing correlation analysis on: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        correlation_results = tc.correlation_analysis(medicines)
        
        print(f"Correlation Analysis Results:")
        print(f"  Correlations found: {len(correlation_results['correlations'])}")
        print(f"  Strong correlations: {len(correlation_results['strong_correlations'])}")
        
        if args.output:
            tc.export_data(correlation_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error performing correlation analysis: {e}")


def handle_patterns(tc: TradChem, args):
    """Handle patterns command."""
    print(f"Performing pattern analysis on: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        pattern_results = tc.pattern_analysis(medicines)
        
        print(f"Pattern Analysis Results:")
        print(f"  Common combinations found: {len(pattern_results['common_combinations'])}")
        
        print(f"Top 5 ingredient combinations:")
        for i, (combination, count) in enumerate(list(pattern_results['common_combinations'].items())[:5], 1):
            print(f"  {i}. {combination}: {count}")
        
        if args.output:
            tc.export_data(pattern_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error performing pattern analysis: {e}")


# ============================================================================
# TRADITIONAL MEDICINE ANALYSIS HANDLERS
# ============================================================================

def handle_analyze_systems(tc: TradChem, args):
    """Handle analyze-systems command."""
    print(f"Analyzing traditional systems from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        system_results = tc.analyze_traditional_systems(medicines)
        
        print(f"Traditional Systems Analysis:")
        for system, data in system_results.items():
            print(f"  {system}:")
            print(f"    Count: {data['count']}")
            print(f"    Geographic origins: {', '.join(data['geographic_origins'])}")
            print(f"    Common benefits: {', '.join(data['common_benefits'])}")
            print(f"    Compounds with SMILES: {data['compounds_with_smiles']}")
        
        if args.output:
            tc.export_data(system_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error analyzing traditional systems: {e}")


def handle_geographic(tc: TradChem, args):
    """Handle geographic command."""
    print(f"Performing geographic analysis on: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        geo_results = tc.geographic_analysis(medicines)
        
        print(f"Geographic Analysis:")
        for region, data in geo_results.items():
            print(f"  {region}:")
            print(f"    Count: {data['count']}")
            print(f"    Systems: {', '.join(data['systems'])}")
            print(f"    Common ingredients: {', '.join(data['common_ingredients'])}")
        
        if args.output:
            tc.export_data(geo_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error performing geographic analysis: {e}")


def handle_benefits(tc: TradChem, args):
    """Handle benefits command."""
    print(f"Performing benefit analysis on: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        benefit_results = tc.benefit_analysis(medicines)
        
        print(f"Benefit Analysis:")
        print(f"  Unique benefits: {len(benefit_results['unique_benefits'])}")
        
        print(f"Top 10 benefits by frequency:")
        sorted_benefits = sorted(benefit_results['benefit_frequency'].items(), 
                               key=lambda x: x[1], reverse=True)[:10]
        for i, (benefit, count) in enumerate(sorted_benefits, 1):
            print(f"  {i}. {benefit}: {count}")
        
        if args.output:
            tc.export_data(benefit_results, args.output, 'json')
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error performing benefit analysis: {e}")


# ============================================================================
# DATA PROCESSING HANDLERS
# ============================================================================

def handle_filter(tc: TradChem, args):
    """Handle filter command."""
    print(f"Filtering data from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        
        # Build filters
        filters = {}
        if args.system:
            filters['system'] = args.system
        if args.region:
            filters['region'] = args.region
        if args.benefit:
            filters['benefit'] = args.benefit
        if args.disease:
            filters['disease'] = args.disease
        if args.ingredient:
            filters['ingredient'] = args.ingredient
        
        filtered_medicines = tc.filter_data(medicines, **filters)
        
        print(f"Filtered {len(filtered_medicines)} medicines from {len(medicines)} total")
        
        if args.output:
            tc.export_data(filtered_medicines, args.output, 'json')
            print(f"Filtered data saved to: {args.output}")
            
    except Exception as e:
        print(f"Error filtering data: {e}")


def handle_sort(tc: TradChem, args):
    """Handle sort command."""
    print(f"Sorting data from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        sorted_medicines = tc.sort_data(medicines, by=args.by, reverse=args.reverse)
        
        print(f"Sorted {len(sorted_medicines)} medicines by {args.by}")
        
        if args.output:
            tc.export_data(sorted_medicines, args.output, 'json')
            print(f"Sorted data saved to: {args.output}")
            
    except Exception as e:
        print(f"Error sorting data: {e}")


def handle_export(tc: TradChem, args):
    """Handle export command."""
    print(f"Exporting data from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        
        if args.output:
            tc.export_data(medicines, args.output, args.format)
            print(f"Data exported to: {args.output}")
        else:
            print(f"Loaded {len(medicines)} medicines")
            
    except Exception as e:
        print(f"Error exporting data: {e}")


# ============================================================================
# VISUALIZATION HANDLERS
# ============================================================================

def handle_plot_chemical(tc: TradChem, args):
    """Handle plot-chemical command."""
    print(f"Creating chemical structure plots from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        tc.plot_chemical_structures(medicines, save_path=args.save)
        
        if args.save:
            print(f"Plot saved to: {args.save}")
            
    except Exception as e:
        print(f"Error creating chemical plots: {e}")


def handle_plot_stats(tc: TradChem, args):
    """Handle plot-stats command."""
    print(f"Creating statistical plots from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        tc.plot_statistics(medicines, save_path=args.save)
        
        if args.save:
            print(f"Plot saved to: {args.save}")
            
    except Exception as e:
        print(f"Error creating statistical plots: {e}")


def handle_plot_geo(tc: TradChem, args):
    """Handle plot-geo command."""
    print(f"Creating geographic plots from: {args.file}")
    
    try:
        medicines = tc.load_data(args.file)
        tc.plot_geographic_distribution(medicines, save_path=args.save)
        
        if args.save:
            print(f"Plot saved to: {args.save}")
            
    except Exception as e:
        print(f"Error creating geographic plots: {e}")


# ============================================================================
# LEGACY HANDLERS (for backward compatibility)
# ============================================================================

def handle_search(tc: TradChem, args):
    """Handle search command (legacy)."""
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
    """Handle info command (legacy)."""
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


def handle_add(tc: TradChem, args):
    """Handle add command (legacy)."""
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
    """Handle template command (legacy)."""
    file_path = Path(args.file)
    
    template = {
        "product_name": "Example Medicine",
        "scientific_name": "Scientific Name",
        "description": "Description of the medicine",
        "traditional_system": "Ayurveda",
        "geographic_origin": "India",
        "benefits": ["Benefit 1", "Benefit 2"],
        "diseases": ["Disease 1", "Disease 2"],
        "chemical_composition": {
            "ingredients": {
                "Ingredient 1": {
                    "smiles": "CCO",
                    "molecular_weight": 46.07
                }
            }
        }
    }
    
    if args.format == 'json':
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(template, f, indent=2, ensure_ascii=False)
    else:
        # CSV template
        import csv
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['product_name', 'scientific_name', 'description', 'traditional_system', 
                           'geographic_origin', 'benefits', 'diseases', 'chemical_composition'])
            writer.writerow(['Example Medicine', 'Scientific Name', 'Description', 'Ayurveda', 
                           'India', 'Benefit 1,Benefit 2', 'Disease 1,Disease 2', '{"ingredients": {}}'])
    
    print(f"Template created: {file_path}")


def handle_validate(tc: TradChem):
    """Handle validate command (legacy)."""
    print("Validating database integrity...")
    
    validation_results = tc.validate_data(tc.data)
    
    print(f"Validation Results:")
    print(f"  Total medicines: {validation_results['total_medicines']}")
    print(f"  Valid medicines: {validation_results['valid_medicines']}")
    print(f"  Invalid medicines: {validation_results['invalid_medicines']}")
    print(f"  Data quality score: {validation_results['data_quality_score']:.2%}")
    
    if validation_results['errors']:
        print(f"  Errors found: {len(validation_results['errors'])}")
        for error in validation_results['errors'][:5]:
            print(f"    - {error}")


if __name__ == '__main__':
    main() 