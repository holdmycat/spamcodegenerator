//
//  AppDelegate.h
//  testSpamCode
//
//  Created by zhao xuefei on 2020/3/11.
//  Copyright © 2020 zhao xuefei. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <CoreData/CoreData.h>

@interface AppDelegate : UIResponder <UIApplicationDelegate>

@property (readonly, strong) NSPersistentContainer *persistentContainer;

- (void)saveContext;


-(UISlider*)overexerted:(UISlider*)hateless ;
@end

