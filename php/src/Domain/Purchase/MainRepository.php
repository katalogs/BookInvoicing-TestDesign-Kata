<?php

namespace Katalogs\BookInvoicing\Domain\Purchase;

class MainRepository
{
    private static Repository $runningRepository;

    public static function configuredRepository(): Repository
    {
        if (self::$runningRepository == null) {
            self::$runningRepository = new JsonRepository();
        }
        return self::$runningRepository;
    }

    // TESTING ONLY
    public static function override(Repository $newRepository): void {
        self::$runningRepository = $newRepository;
    }

    // TESTING ONLY
    public static function reset(): void {
        self::$runningRepository = new JsonRepository();
    }
}