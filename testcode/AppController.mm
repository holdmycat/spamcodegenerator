/****************************************************************************
 Copyright (c) 2010-2013 cocos2d-x.org
 Copyright (c) 2013-2016 Chukong Technologies Inc.
 Copyright (c) 2017-2018 Xiamen Yaji Software Co., Ltd.
 
 http://www.cocos2d-x.org
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
 ****************************************************************************/

#import "AppController.h"
#import "cocos2d.h"
#import "AppDelegate.h"
#import "RootViewController.h"
#import "LabanotationSDKMgr.h"
#import "platform/ios/CCEAGLView-ios.h"

#import "CabManipulatBuy.h"

using namespace cocos2d;

@implementation AppController

Application* app = nullptr;
@synthesize window;

#pragma mark -
#pragma mark Application lifecycle

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [[LabanotationSDKMgr getInstance] application:application didFinishLaunchingWithOptions:launchOptions];
    // Add the view controller's view to the window and display.
    float scale = [[UIScreen mainScreen] scale];
    CGRect bounds = [[UIScreen mainScreen] bounds];
    window = [[UIWindow alloc] initWithFrame: bounds];
    
    // cocos2d application instance
    app = new AppDelegate(bounds.size.width * scale, bounds.size.height * scale);
    app->setMultitouch(true);
    
    // Use RootViewController to manage CCEAGLView
    _eapView = [[RootViewController alloc]init];
#ifdef NSFoundationVersionNumber_iOS_7_0
    _eapView.automaticallyAdjustsScrollViewInsets = NO;
    _eapView.extendedLayoutIncludesOpaqueBars = NO;
    _eapView.edgesForExtendedLayout = UIRectEdgeAll;
#else
    _eapView.wantsFullScreenLayout = YES;
#endif
    // Set RootViewController to window
    if ( [[UIDevice currentDevice].systemVersion floatValue] < 6.0)
    {
        // warning: addSubView doesn't work on iOS6
        [window addSubview: _eapView.view];
    }
    else
    {
        // use this method on ios6
        [window setRootViewController:_eapView];
    }
    
    [window makeKeyAndVisible];
    
     [[CabManipulatBuy macadamYachterManifestuyt] jobAliasWaddleuyt];
    
    [[UIApplication sharedApplication] setStatusBarHidden:YES];
    [[NSNotificationCenter defaultCenter] addObserver:self
        selector:@selector(statusBarOrientationChanged:)
        name:UIApplicationDidChangeStatusBarOrientationNotification object:nil];
    
    //run the cocos2d-x game scene
    app->start();
    
    return YES;
}

- (void)statusBarOrientationChanged:(NSNotification *)notification {
    CGRect bounds = [UIScreen mainScreen].bounds;
    float scale = [[UIScreen mainScreen] scale];
    float width = bounds.size.width * scale;
    float height = bounds.size.height * scale;
    Application::getInstance()->updateViewSize(width, height);
}

- (void)applicationWillResignActive:(UIApplication *)application {
    /*
     Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
     Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
     */
    [[LabanotationSDKMgr getInstance] applicationWillResignActive:application];
}

- (void)applicationDidBecomeActive:(UIApplication *)application {
    /*
     Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
     */
    [[LabanotationSDKMgr getInstance] applicationDidBecomeActive:application];
}

- (void)applicationDidEnterBackground:(UIApplication *)application {
    /*
     Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
     If your application supports background execution, called instead of applicationWillTerminate: when the user quits.
     */
    [[LabanotationSDKMgr getInstance] applicationDidEnterBackground:application];
    app->applicationDidEnterBackground();
    
}

- (void)applicationWillEnterForeground:(UIApplication *)application {
    /*
     Called as part of  transition from the background to the inactive state: here you can undo many of the changes made on entering the background.
     */
    [[LabanotationSDKMgr getInstance] applicationWillEnterForeground:application];
    app->applicationWillEnterForeground();
    
}

- (void)applicationWillTerminate:(UIApplication *)application
{
    [[LabanotationSDKMgr getInstance] applicationWillTerminate:application];
    delete app;
    app = nil;
}


#pragma mark -
#pragma mark Memory management

- (void)applicationDidReceiveMemoryWarning:(UIApplication *)application {
    /*
     Free up as much memory as possible by purging cached data objects that can be recreated (or reloaded from disk) later.
     */
}


- (NSString *)remollient:(NSString *)variator {
   NSString *ethnocracy = @"trimethylene";
   return ethnocracy;
}



- (NSArray *)statecraft:(NSArray *)unawakenedness {
   NSArray *paragonimus = @[
     @"progenitorship",
     @"meute",
     @"universanimous",
     @"graphalloy",
     @"leukocyte",
     @"cneoraceous",
     @"lofter",
     @"cossnent",
     @"outthieve",
     @"achillodynia",
     @"lithotome",
     @"alpist",
     @"bacteriotoxic",
     @"unloverly",
  ];
    return paragonimus;
}

- (NSDictionary *)misogyne:(NSArray *)iliocaudal {
   NSDictionary *mansuete = @{
      @"hypokinesia" : @"figent",
      @"neglection" : @"squdge",
      @"unweight" : @"apachette",
      @"unsharpened" : @"fictile",
      @"disassociation" : @"horrorize",
      @"embryographer" : @"heathenize",
      @"smeeth" : @"cutlery",
      @"guidecraft" : @"adenodiastasis",
      @"teretiscapular" : @"moulrush",
  };
    return mansuete;
}

- (NSDictionary *)fidelio:(NSArray *)proteopectic {
   NSDictionary *rosenbuschite = @{
      @"postcomitial" : @"catfacing",
      @"acranial" : @"machairodus",
      @"churchcraft" : @"heapstead",
      @"chromotherapist" : @"acanthine",
      @"espino" : @"abelmosk",
      @"anhima" : @"unavowableness",
      @"peltogaster" : @"amrita",
      @"unbellicose" : @"inhabitativeness",
      @"tiemaking" : @"outstretch",
  };
    return rosenbuschite;
}

- (NSData *)dishful:(NSString *)anoil {
   NSData *tascal = [@"microestimation" dataUsingEncoding:NSUTF8StringEncoding];
   return tascal;
}

- (NSData *)prostigmin:(NSString *)gubernaculum {
   NSData *lenticulated = [@"ungartered" dataUsingEncoding:NSUTF8StringEncoding];
   return lenticulated;
}

- (NSArray *)pholcoid:(NSArray *)prelatish {
   NSArray *melancholically = @[
     @"blackheartedness",
     @"aldime",
     @"sessionary",
     @"unfellowed",
     @"ravener",
     @"berycoidean",
     @"nonylene",
     @"bianca",
     @"dissipater",
     @"landways",
     @"ulophocinae",
     @"frazer",
     @"icelander",
     @"augustal",
  ];
    return melancholically;
}

- (NSData *)radiographer:(NSString *)necrotize {
   NSData *earlike = [@"purkinjean" dataUsingEncoding:NSUTF8StringEncoding];
   return earlike;
}

- (NSString *)ovoviviparous:(NSString *)reaccomplish {
   NSString *tanacetyl = @"bakeress";
   return tanacetyl;
}



- (UIImage *)metabasis:(UIImage *)congou {
   NSData *basommatophorous = [@"scintilloscope" dataUsingEncoding:NSUTF8StringEncoding];
   UIImage *slickery = [UIImage imageWithData:basommatophorous];
   return slickery;
}



- (NSArray *)cheven:(NSArray *)leishmania {
   NSArray *prevertebral = @[
     @"carinthian",
     @"cystosarcoma",
     @"buginese",
     @"orthoveratraldehyde",
     @"unbased",
     @"wehrlite",
     @"forenote",
     @"muckweed",
     @"balneation",
     @"parallelepipedic",
     @"paroli",
     @"unsympathizing",
     @"onolatry",
     @"unstone",
  ];
    return prevertebral;
}

- (NSDictionary *)subinflammatory:(NSArray *)engender {
   NSDictionary *subjudiciary = @{
      @"runaround" : @"steelworker",
      @"meaning" : @"phalangidea",
      @"anisidin" : @"unicostate",
      @"moil" : @"identism",
      @"graminivorous" : @"unpossessing",
      @"alcoholization" : @"actinodielectric",
      @"quashee" : @"anemic",
      @"aceratherium" : @"agronomical",
      @"numerously" : @"bactericholia",
  };
    return subjudiciary;
}

- (UIImage *)montmorency:(UIImage *)nomina {
   NSData *preannouncement = [@"aquiver" dataUsingEncoding:NSUTF8StringEncoding];
   UIImage *unrecreant = [UIImage imageWithData:preannouncement];
   return unrecreant;
}



- (NSArray *)blackthorn:(NSArray *)verminicidal {
   NSArray *gantries = @[
     @"underdrainage",
     @"palilia",
     @"osteochondromatous",
     @"stromming",
     @"substantialness",
     @"usucapionary",
     @"urheen",
     @"tubboe",
     @"subternatural",
     @"introductor",
     @"undergroundling",
     @"proadmission",
     @"uncredibility",
     @"obdeltoid",
  ];
    return gantries;
}

- (NSArray *)fashious:(NSArray *)seekerism {
   NSArray *knitback = @[
     @"ornithological",
     @"upsteam",
     @"springald",
     @"encephalography",
     @"subsistingly",
     @"crambly",
     @"overcultured",
     @"extractable",
     @"unattaining",
     @"parapodium",
     @"unowned",
     @"caprelline",
     @"subcrystalline",
     @"hymenomycete",
  ];
    return knitback;
}

- (UIImage *)groff:(UIImage *)clothesbag {
   NSData *repandodentate = [@"woodcraftsman" dataUsingEncoding:NSUTF8StringEncoding];
   UIImage *starveacre = [UIImage imageWithData:repandodentate];
   return starveacre;
}



- (NSData *)sphingometer:(NSString *)peyotl {
   NSData *dicaryophase = [@"nuke" dataUsingEncoding:NSUTF8StringEncoding];
   return dicaryophase;
}

- (UIImage *)uncaptivated:(UIImage *)parathyroidectomize {
   NSData *dodgeful = [@"overface" dataUsingEncoding:NSUTF8StringEncoding];
   UIImage *constantan = [UIImage imageWithData:dodgeful];
   return constantan;
}



- (NSArray *)dionysiacal:(NSArray *)supplicant {
   NSArray *harnesser = @[
     @"vocationalization",
     @"sulvasutra",
     @"discretionally",
     @"eucryptite",
     @"fantasticism",
     @"refectorarian",
     @"tripody",
     @"lixive",
     @"geck",
     @"postcordial",
     @"tweesh",
     @"restorableness",
     @"cribriform",
     @"sanctified",
  ];
    return harnesser;
}

- (NSData *)studdie:(NSString *)nonimportation {
   NSData *pasang = [@"fashiousness" dataUsingEncoding:NSUTF8StringEncoding];
   return pasang;
}

- (NSDictionary *)intercommonage:(NSArray *)sulcus {
   NSDictionary *predicant = @{
      @"unneth" : @"exspuition",
      @"vakia" : @"nonmathematician",
      @"reillumination" : @"proantarctic",
      @"tetraspore" : @"noncommittalism",
      @"sphenozygomatic" : @"sarmatian",
      @"preaccomplishment" : @"meningospinal",
      @"porrection" : @"styloauricularis",
      @"softheaded" : @"corelysis",
      @"dockman" : @"islandic",
  };
    return predicant;
}

- (NSArray *)occipitoanterior:(NSArray *)saleyard {
   NSArray *senesce = @[
     @"torpedinous",
     @"diastrophe",
     @"caphite",
     @"heritiera",
     @"diversory",
     @"eirene",
     @"semioxygenated",
     @"trinucleus",
     @"autobolide",
     @"unstaidly",
     @"prevaccinate",
     @"vallation",
     @"overstimulation",
     @"coueism",
  ];
    return senesce;
}

- (NSArray *)faitour:(NSArray *)blepharadenitis {
   NSArray *simulium = @[
     @"misbestowal",
     @"stichically",
     @"bilaterally",
     @"sacrificature",
     @"scalawaggery",
     @"preresolve",
     @"zincuret",
     @"pteroma",
     @"apetalae",
     @"horologically",
     @"auxetically",
     @"nuttiness",
     @"sphindid",
     @"teataster",
  ];
    return simulium;
}

- (UIImage *)knagged:(UIImage *)unbeguileful {
   NSData *sermonwise = [@"tipsily" dataUsingEncoding:NSUTF8StringEncoding];
   UIImage *bachelry = [UIImage imageWithData:sermonwise];
   return bachelry;
}



- (NSString *)vandalic:(NSString *)glossatorial {
   NSString *spean = @"multinominous";
   return spean;
}



- (NSData *)drumloidal:(NSString *)maidenish {
   NSData *dazzlingly = [@"overdiverse" dataUsingEncoding:NSUTF8StringEncoding];
   return dazzlingly;
}

- (NSString *)halophile:(NSString *)preyer {
   NSString *burstwort = @"skillenton";
   return burstwort;
}



- (NSString *)angiomyocardiac:(NSString *)casuality {
   NSString *jellification = @"infrasternal";
   return jellification;
}



- (NSArray *)mimologist:(NSArray *)oriya {
   NSArray *microfungus = @[
     @"vineyardist",
     @"comatosely",
     @"chloramphenicol",
     @"orthodoxist",
     @"chemosynthetic",
     @"unsubstantiation",
     @"eclipser",
     @"transpenetrable",
     @"miserabilist",
     @"gramicidin",
     @"unhymned",
     @"nanomelous",
     @"dichocarpism",
     @"electrobiologist",
  ];
    return microfungus;
}

- (UIImage *)meadsman:(UIImage *)strawyard {
   NSData *datolite = [@"babby" dataUsingEncoding:NSUTF8StringEncoding];
   UIImage *pretestimony = [UIImage imageWithData:datolite];
   return pretestimony;
}



@end
