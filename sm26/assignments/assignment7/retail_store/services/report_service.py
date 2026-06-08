import json


class ReportServices:
    
    def save_report(self, report_name: str, data:any, path:str='reports/report.txt')->None:
        with open(path, 'a') as file:
            file.write(f'Report name: {report_name}')
            file.write(json.dumps(data, indent=4))
            file.write('\n')
        print(f'{report_name} saved to {path}')
        #this will save our report to report.txt
        
    #now to generate summary
    def generate_summary(self, 
                         total_customers:int,
                         total_transactions: int, 
                         total_revenue: int, 
                         highest_spender: str, 
                         lowest_spender: str, 
                         popular_category: str,
                         filepath: str = 'reports/summary.txt')->None:
        
        with open(filepath, 'w') as file:
            summary_text = f''' Total Customers: {total_customers}\n
Total Transactions: {total_transactions}\n
Total Revenue: {total_revenue}\n
Highest Spender: {highest_spender}\n
Lowest Spender: {lowest_spender}\n
Popular Catagory: {popular_category}'''
                                
            file.write(summary_text)   
        print(f'Buisness summary saved to {filepath}') 