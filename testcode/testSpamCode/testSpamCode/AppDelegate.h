//
//  AppDelegate.h
//  testSpamCode
//
//  Created by zhao xuefei on 2020/3/11.
//  Copyright © 2020 zhao xuefei. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import <CoreData/CoreData.h>

@interface AppDelegate : NSObject <NSApplicationDelegate>

@property (readonly, strong) NSPersistentContainer *persistentContainer;


@end

