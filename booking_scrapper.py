from playwright.sync_api import sync_playwright
import pandas as pd


def main():
    
    with sync_playwright() as p:
        
        #Change dates to future dates, otherwise it won't work
        checkin_date = '2024-08-17'
        checkout_date = '2023-08-18'
        
        page_url = f'https://www.booking.com/searchresults.en-gb.html?checkin={checkin_date}&checkout={checkout_date}&ss=Kathmandu&ssne=Kathmandu&ssne_untouched=Kathmandu&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaKsBiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAL6jIK2BsACAdICJGI5MTYxMWNiLWFhMGEtNDc3Yy04MzNkLWI1NjdhMWMwOTA4ZNgCBeACAQ&sid=388e41ac705c2a1e7e6963fd39ea005f&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-1022136&dest_type=city&checkin=2024-08-18&checkout=2024-08-19&group_adults=2&no_rooms=1&group_children=0'

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(page_url, timeout=60000)
                    
        hotels = page.locator('//div[@data-testid="property-card"]').all()
        print(f'There are: {len(hotels)} hotels.')

        hotels_list = []
        for hotel in hotels:
            hotel_dict = {}
            hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
            hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]

            hotels_list.append(hotel_dict)
        
        df = pd.DataFrame(hotels_list)
        df.to_excel('hotels.xlsx', index=False) 
        df.to_csv('hotels_data.csv', index=False) 
        
        browser.close()
            
if __name__ == '__main__':
    main()