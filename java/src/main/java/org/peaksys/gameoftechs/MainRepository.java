package org.peaksys.gameoftechs;

import org.peaksys.gameoftechs.storage.JsonRepository;
import org.peaksys.gameoftechs.storage.Repository;

public final class MainRepository {

    private static Repository runningRepository;

    private MainRepository() {
    }

    public static Repository configuredRepository() {
        if (runningRepository == null) {
            runningRepository = new JsonRepository();
        }
        return runningRepository;
    }

    /* Working effectively with Legacy Code
     * https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code
     */
    // TESTING ONLY
    public static void override(Repository newRepository) {
        runningRepository = newRepository;
    }

    // TESTING ONLY
    public static void reset() {
        runningRepository = new JsonRepository();
    }
}
