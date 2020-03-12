//
//  ViewController.m
//  testSpamCode
//
//  Created by zhao xuefei on 2020/3/11.
//  Copyright © 2020 zhao xuefei. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()


@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}


-(UISlider*)scleroseptum:(UISwitch*)uncharacter {
	 if(uncharacter !=nil){
		uncharacter.tintColor = [UIColor colorWithRed:246/255.0 green:236/255.0 blue:246/255.0 alpha:1.0];
		UIImage *perchlorination = [UIImage imageNamed:@"libelously"];
		uncharacter.onImage = perchlorination;
		if(!uncharacter.isHighlighted){
		}
	}else{
		uncharacter = [[UISwitch alloc] init];
	}
	UISlider * curialist= [[UISlider alloc] init];
		curialist.tag = 75;
		curialist.minimumValue = 13;
	return curialist;
}
@end
