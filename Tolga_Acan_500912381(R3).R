library(tidyverse)
library(tidymodels)
library(caret)

house <- read.csv("https://www.dropbox.com/s/tvvtf9dwjufo7os/housing_train.csv?dl=1")

set.seed(4)
split_obj <- initial_split(house, .7 )

train_set <- training(split_obj)
test_set <- testing(split_obj)

train_set_sf <- select(train_set, contains("sf"), SalePrice )

baseline_model <- lm(SalePrice ~ ., data = train_set_sf )

train_base_pred <- predict(baseline_model, train_set)
baseline_pred <- predict(baseline_model, test_set)

RMSE(train_base_pred, train_set$SalePrice )
RMSE(baseline_pred, test_set$SalePrice )

train_set_sf2 <- mutate( train_set_sf ,
                         total_sf = TotalBsmtSF + X1stFlrSF + X2ndFlrSF + 
                          LowQualFinSF + WoodDeckSF + OpenPorchSF)

test_set2 <- mutate( test_set ,
                         total_sf = TotalBsmtSF + X1stFlrSF + X2ndFlrSF + 
                           LowQualFinSF + WoodDeckSF + OpenPorchSF)

ggplot(train_set_sf3, aes(total_sf, SalePrice) ) +
  geom_point()

train_set_sf3 <- subset(train_set_sf2, total_sf < 7500)


rf_mod <- train(SalePrice~., data = train_set_sf3, method = "rf")
rf_mod
plot(rf_mod)
cube_mod <- train(SalePrice ~ ., data = train_set_sf3, method ="cubist")

plot(cube_mod)

trctrl <- trainControl(method = "cv", number = 10, verboseIter = TRUE)
cube_mod2 <- train(SalePrice ~ ., data = train_set_sf3, method ="cubist", trControl = trctrl)

plot (cube_mod2)
train_set2 <- select(train_set, contains("sf"), contains("area"), "SalePrice" )
train_set2 <- na.omit(train_set2)



#principle component analysis
race_pca <- recipe(SalePrice ~ ., data = select(train_set, contains("sf"), contains("area"), "SalePrice" )) %>%
  step_bagimpute(all_predictors()) %>%
  step_normalize(all_predictors()) %>%
  step_pca(all_numeric(),-SalePrice) %>% 
  prep()

train_pca <- bake(race_pca, train_set)
head(train_pca)
ggplot(train_pca, aes(PC1,PC2)) +
  geom_point()

test_pca <- bake(race_pca, test_set)

cube_mod2 <- train(SalePrice ~ ., data = train_pca, method ="cubist", trControl = trctrl)
plot(cube_mod2)

#Note: using pca is an effective way to model a dataset

